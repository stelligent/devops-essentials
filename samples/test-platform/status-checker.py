# IMPORTS----------------------------------------------
import boto3

# VARIABLES--------------------------------------------
# DO NOT CHANGE stack_name as it's a key.
stack_name = 'StackName'
default_region = 'us-east-1'
failure_states = ['CREATE_FAILED', 'ROLLBACK_COMPLETE','ROLLBACK_IN_PROGRESS','UPDATE_ROLLBACK_FAILED','UPDATE_ROLLBACK_IN_PROGRESS','ROLLBACK_FAILED']
success_states = ['CREATE_COMPLETE','UPDATE_COMPLETE','UPDATE_COMPLETE_CLEANUP_IN_PROGRESS']
in_progress_states = ['CREATE_IN_PROGRESS','REVIEW_IN_PROGRESS','UPDATE_IN_PROGRESS']
# CHANGE the strings BELOW to the stacks you want to check
# stacks_to_be_checked uses cfn stack NAMES
stacks_to_be_checked = ['ForThePeople-backend-rjulian', 'mu-repo-munatra']
# stack_id uses cfn stack IDs
stack_id = ['arn:aws:cloudformation:us-east-1:324320755747:stack/ForThePeople-backend-rjulian/9403bf90-8770-11e7-8326-500c2854e035']

# FUNCTIONS--------------------------------------------
# Returns a dictionary holding all of the various stacks' info
# DOES NOT RETURN DELETED STACKS' INFO!!!
def get_all_stacks_info():
	client = boto3.client('cloudformation')
	# response is a dict
	response = client.list_stacks(
    	StackStatusFilter=[
        	'CREATE_IN_PROGRESS','CREATE_FAILED','CREATE_COMPLETE','ROLLBACK_IN_PROGRESS','ROLLBACK_FAILED','ROLLBACK_COMPLETE','UPDATE_IN_PROGRESS','UPDATE_COMPLETE_CLEANUP_IN_PROGRESS','UPDATE_COMPLETE','UPDATE_ROLLBACK_IN_PROGRESS','UPDATE_ROLLBACK_FAILED','UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS','UPDATE_ROLLBACK_COMPLETE','REVIEW_IN_PROGRESS',
    	]
	)
	return response

# Returns a list of all the stack names currently in cfn
def get_all_stack_names():
	# print response['StackSummaries'][0]['StackName']
	list_of_stack_names = []
	response = get_all_stacks_info()
	for key in response['StackSummaries']:
		if stack_name in key:
			# print key[stack_name]
			# for one_stack in stacks_to_be_checked:
			# 	if key[stack_name] == one_stack:
			# 		print one_stack
			list_of_stack_names.append(key[stack_name])
	return list_of_stack_names

# def check_status_of_stack_names(stacks_to_be_checked):
# 	all_stacks_names = get_all_stack_names()
# 	for one_stack in stacks_to_be_checked:
# 		if one_stack in all_stacks_names:
			

# check_status_of_stack_names(stacks_to_be_checked)
print ''
print '******************************************'
print ''
# THE HARD CODED VERSION USING STACK_ID
resource = boto3.resource('cloudformation')

# status = resource.Stack('arn:aws:cloudformation:us-east-1:324320755747:stack/ForThePeople-backend-rjulian/9403bf90-8770-11e7-8326-500c2854e035').stack_status
# print status

def get_status_using_stack_ids(stack_id):
	list_of_status = []
	for x in stack_id:
		status = resource.Stack(x).stack_status
		list_of_status.append(status)
	return list_of_status


# TESTS-----------------------------------

def test_get_all_stacks_info():
	response = get_all_stacks_info()
	print response


def test_get_all_stack_names():
	all_the_stacks = get_all_stack_names()
	for x in all_the_stacks:
		print x

def test_get_status_using_stack_ids(stack_id):
	all_the_status = get_status_using_stack_ids(stack_id)
	print all_the_status

# test_get_all_stacks_info()
# test_get_all_stack_names()
# test_get_status_using_stack_ids(stack_id)


print ''
print '************************************************************'
print ''

# FUTURE TO DO: change 'in' to 'set' or 'bisect' for faster processing time
all_my_stack_status = get_status_using_stack_ids(stack_id)
for one_status in all_my_stack_status:
	if one_status in success_states:
		print 'The stack was created succeessfully'
	if one_status in failure_states:
		print 'The stack creation failed'
	if one_status in in_progress_states:
		print 'The stack creation is in progress'

