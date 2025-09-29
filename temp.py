import bcrypt

db_password = b"$2b$15$2s82yGetKOiSqY6nez12BOAlwSDKGCngL7hGpxbX9Er62y0paFPxW"  # copy from DB
print(bcrypt.checkpw(b"alice123", db_password))
