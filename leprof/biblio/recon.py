import pandas as pd
from tqdm import tqdm
from biblio import book
from biblio import work
tqdm.pandas()
class Recon:
    def __init__(self):
        self.booksfr = None
        self.booksfr_recon = None

    def works_reconciliation(self, source_filename: str=None)->(pd.DataFrame, pd.DataFrame):
        if not source_filename:
            source_filename = '../data/booksfr-full.json'
        try:
            self.booksfr = pd.read_json(source_filename)
        except ValueError:
            self.booksfr = pd.read_json(source_filename, lines=True)
        self.booksfr ['title_normalized'] = self.booksfr ['title'].progress_apply(lambda x: book.Book.normalize_title(title=x))
        self.booksfr ['authors_normalized'] = self.booksfr ['authors'].progress_apply(
            lambda x: book.Book.normalize_authors(authors=x))
        self.booksfr_recon = self.booksfr[["id_ean", "title_normalized", "authors_normalized"]]
        self.booksfr_recon = self.booksfr_recon.assign(
            workid=self.booksfr_recon.groupby(["title_normalized", "authors_normalized"]).ngroup())
        self.booksfr_recon.to_csv('booksfr_recon.csv', index=False, sep=',')
        self.booksfr_recon['workid'] = self.booksfr_recon['workid'].progress_apply(
            lambda x: work.Work.gererate_workid_from(source=str(x)))
        return self.booksfr, self.booksfr_recon

    def show_performance(self)-> None:
        perf_booksfr = self.booksfr.groupby(['glid']).count().sort_values('id_ean').groupby(['id_ean']).count()['title']
        perf_booksfr_recon = self.booksfr_recon.groupby(['workid']).count().sort_values('id_ean').groupby(['id_ean']).count()['title_normalized']
        comparatif = pd.concat([perf_booksfr, perf_booksfr_recon], axis=1)
        comparatif['diff'] = comparatif.apply(lambda x: abs(round(((x['title'] - x['title_normalized']) / x['title'])*100,2)), axis=1)
        comparatif.rename(columns={'title': 'gleeph', 'title_normalized': 'myrecon'}, inplace=True)
        print(comparatif)
        print(f"Nombre de livres: {self.booksfr.shape[0]}")
        print(f"Moyenne de différence: {round(comparatif['diff'].mean(),2)}%")