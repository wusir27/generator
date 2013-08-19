# _*_ coding: utf-8 _*_
# vm进程启动shell脚本生成
import os

def main():
	print 'Generating...'
	
	#[目录名,文件名前缀,配置文件名前缀,服务名前缀,调度启动类名]
	
	scheduleInfo = readConfToArray('schedule_info',6)

	#[中心,节点,地市]
	disInfo = readConfToArray('center_host_district',3)
	
	#生成目录
	os.mkdir('newShell')
	for di in disInfo:
		if not os.path.exists('newShell/center'+di[0]):
			os.mkdir('newShell/center'+di[0])
		if not os.path.exists('newShell/center'+di[0]+'/host'+di[1]):
			os.mkdir('newShell/center'+di[0]+'/host'+di[1])
		for dj in scheduleInfo:
			if not os.path.exists('newShell/center'+di[0]+'/host'+di[1]+'/'+dj[0]):
				os.mkdir('newShell/center'+di[0]+'/host'+di[1]+'/'+dj[0])	
				if not os.path.exists('newShell/center'+di[0]+'/host'+di[1]+'/'+dj[0]+'/bin'):
					os.mkdir('newShell/center'+di[0]+'/host'+di[1]+'/'+dj[0]+'/bin')

	
	geneFile('start','start_tf_template',scheduleInfo,disInfo)  #generate start shell
	geneFile('monitor','monitor_tf_template',scheduleInfo,disInfo) #generate monitor shell
	geneFile('stop','stop_tf_template',scheduleInfo,disInfo) #generate stop shell





		
def readConfToArray(path,arrayLength):
	fsr = file(path)
	ret = []
	while True:
		line = fsr.readline()
		if len(line)==0:
			break
		s = line.strip('\n\r').split('#')[0].strip().split(',')
		if len(s) == arrayLength:
			ret.append(s)
	fsr.close()
	return ret

def geneFile(name,templatePath,scheduleInfo,disInfo):
	
	#读取模板
	fr = file(templatePath,'r')
	shellString = ''
	while True:
		line = fr.readline()
		if len(line) == 0:
			break
		shellString += line
	fr.close()
	
	#生成文件
	count = 0
	for i in scheduleInfo:
		for j in disInfo:
			startupClassSplit = i[4].split('.')  #get the className
			startupClass = startupClassSplit[len(startupClassSplit)-1] 
			shell = shellString.replace('<file_name_prefix>',i[1]).replace('<center>',j[0]).replace('<host>',j[1]).replace('<dir_name>',i[0]).replace('<config_file_prefix>',i[2]).replace('<server_name_prefix>',i[3]).replace('<schedule_class_prefix>',i[4]).replace('<district>',j[2]).replace('<startup_class_name>',startupClass).replace('<mem_args>',i[5])
			
			shellFileName = 'newShell/center'+j[0]+'/host'+j[1]+'/'+i[0]+'/bin/'+name+'_tf_'+i[1]+'_cen'+j[0]+'_bd'+j[1]+'_'+j[2]+'.sh'
			fw = file(shellFileName,'w')
			fw.write(shell)
			fw.close()
			print('生成文件:'+shellFileName)
			count = count+1
	print '%d %s files generated.' %(count,name)


if __name__ == '__main__' :
	main()
