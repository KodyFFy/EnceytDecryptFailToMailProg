import dropbox

Token = "jwqEoop4M6IAAAAAAAAAATqRP_UhTzJ2nk6QYRopYpwcg0ncnKbTE8cnwhwjUbb1"

dbx = dropbox.Dropbox(Token)


def upload_file(dbx, loc, file):
	with open(file, "rb") as f:
		dbx.files_upload(f.read(), loc, mode = dropbox.files.WriteMode.overwrite)

def download_file(dbx, loc, file):
	with open(file,"wb") as f:
		metadata, res = dbx.files_download(path = loc)
		f.write(res.content)