#coding=gbk
'''
with���(�����Ĺ�����
with�������Զ�������������Դ������ʲôԭ������with�鶼��ȷ���ļ���ȷ�Ĺرգ��Դ����ﵽ�ͷ���Դ��Ŀ��
'''

print(type(open('a.data','r')))
with open('a.data','r') as file:#open('a.data','r')��仰�Ķ�����������Ĺ�����
    print(file.read())

#����дclose()�ˣ����뿪with���ʱ���Զ��ͷ���Դ


with open('�з�.jpg','rb') as src_file:
    with open('copy.png','wb') as target_file:
        target_file.write(src_file.read())