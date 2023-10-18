from supabase import create_client, Client
import config

supabase_url = ''
supabase_key = config.API_KEYS['supa_pwd']
supabase: Client = create_client(supabase_url, supabase_key)
bucket_name=""

res = supabase.storage.from_(bucket_name).list()

with open(filepath, 'rb') as f:
    supabase.storage.from_(bucket_name).upload(file=f,path=path_on_supastorage)
