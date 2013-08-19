# _*_ coding: utf-8 -*-
#Generate the vm config file
import os

def main():
	print 'generating...'
	#[文件名,队列ID,队列类型前缀]
	#queueBusi = [['confirm_vm_schedule','vm_confirm','CONFIRM_WORKFLOW_'], ['dbsms_vm_schedule','vm_dbsms','DBSMS_WORKFLOW_'], ['ee_vm_schedule','exception','APPFRAME_WORKFLOW_EE_'], ['emergency_vm_schedule','emergency1','APPFRAME_WORKFLOW_EMERGENCY_'], ['group_vm_schedule','vm_group','GROUP_WORKFLOW_'], ['home_vm_schedule','vm_confirm','HOME_WORKFLOW_'], ['vm_dtd_schedule','BEWA','BEWA_'], ['vm_esop_schedule','vm_esop','ESOP_WORKFLOW_'], ['vm_schedule','workflow','APPFRAME_WORKFLOW_'], ['workflow_batch_vm_schedule','workflow_batch','WORKFLOW_BATCH_']] 
	queueBusi = readConfToArray('config_info',3)
	
	#[中心,节点,地市]
	

	#disInfo = [['3','9','A'],['1','1','F'], ['1','2','G'], ['3','7','K'], ['1','2','L'], ['3','8','B'], ['1','3','C'], ['1','3','Q'], ['4','12','R'], ['4','12','E'], ['2','4','H'], ['2','5','N'], ['4','11','D'], ['2','5','S'], ['2','6','J'], ['4','10','P'], ['2','6','M']]
	disInfo = readConfToArray('center_host_district',3)
	
	#读取模板
	configTemp = ''
	fr = file('config_template','r')
	while True:
		line = fr.readline()
		if len(line) == 0:
			break
		configTemp += line
	fr.close()
	
	#创建目录
	os.mkdir('newconfigext')
	
	count = 0
	for i in queueBusi:
		for j in disInfo:
			configString = configTemp.replace('[queue_id]',i[1]).replace('[task_type_prefix]',i[2]).replace('[district]',j[2]).replace('[center]',j[0])
			fileName = 'newconfigext/'+i[0]+'.module.cen'+j[0]+'.bd'+j[1]+'.'+j[2]
			f = file(fileName,'w')
			f.write(configString)
			f.close()
			print 'generate file: '+fileName
			count += 1

	print '%d files generated.'%(count)
	print 'generated.'



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
        fsr.close
        return ret

if __name__ == '__main__':
	main()
