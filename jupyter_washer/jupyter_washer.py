# coding: utf-8

def pls_wash(file_path=None,backup=True):
    if file_path==None: file_path = raw_input("Enter the path of your script:")
    import os 
    import shutil
    with open(file_path,'r+',encoding='utf-8') as f: 
        if backup==True:
            backup_file = os.path.normpath(os.path.join(os.path.dirname(file_path),'backup_'+os.path.basename(file_path)))
            shutil.copyfile(file_path,backup_file)
            print('A back-up copy has been saved at',backup_file+'\n')
        codes = [i for i in f.readlines() if not i.startswith('# In[')]
        row_num = 0
        last_row_content = None
        cleaned_codes = []
        for line in codes:
            if row_num>0 and len(line.strip())==0 and len(last_row_content.strip())==0: pass
            else: cleaned_codes.append(line)
            row_num+=1
            last_row_content=line
        f.seek(0)
        f.truncate()
        f.writelines(cleaned_codes)
        print( 'Mission complete!'+'\n'+'Your script has been cleaned!'+'\n'+'See %s'%file_path)
		
if __name__ == "__main__":
	import sys
	pls_wash(sys.argv[1])
