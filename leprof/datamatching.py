from biblio import recon

""" 
booksdef = pd.read_json('../data/booksfr.json')
booksdef['title_normalized'] = booksdef['title'].progress_apply(lambda x: book.Book.normalize_title(title=x))
booksdef['authors_normalized'] = booksdef['authors'].progress_apply(lambda x: book.Book.normalize_authors(authors=x))
print(booksdef.head())
booksdef.to_csv('booksfr_normalized.csv', index=False, sep=',')
booksrecon = booksdef[["id_ean", "title_normalized", "authors_normalized"]]
booksrecons_wt_workid = booksrecon.assign(workid = booksrecon.groupby(["title_normalized", "authors_normalized"]).ngroup())
print(booksrecons_wt_workid.head())
booksrecons_wt_workid.to_csv('booksfr_recon.csv', index=False, sep=',')
booksrecons_wt_workid['workid'] = booksrecons_wt_workid['workid'].apply(lambda x: work.Work.gererate_workid_from(source=str(x)))
print(booksrecons_wt_workid.head())
"""
gleeph_recon = recon.Recon()
df_gleeph, df_recon = gleeph_recon.works_reconciliation()
gleeph_recon.show_performance()