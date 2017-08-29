# THIS ENTIRE PROGRAM DOES NOT LOOK AT OR FOR DELETED STACKS
# You must change the string in the first function, get_stacks_to_be_tested(),
# to a part of the name of the cfn stacks you'd like to check.

# IMPORTS----------------------------------------------
import boto3


# VARIABLES--------------------------------------------
# DO NOT CHANGE stack_name or stack_status as they're keys.
stack_name = 'StackName'
stack_status = 'StackStatus'
default_region = 'us-east-1'
failure_states = ['CREATE_FAILED', 'ROLLBACK_COMPLETE','ROLLBACK_IN_PROGRESS','UPDATE_ROLLBACK_FAILED','UPDATE_ROLLBACK_IN_PROGRESS','ROLLBACK_FAILED']
success_states = ['CREATE_COMPLETE','UPDATE_COMPLETE','UPDATE_COMPLETE_CLEANUP_IN_PROGRESS']
in_progress_states = ['CREATE_IN_PROGRESS','REVIEW_IN_PROGRESS','UPDATE_IN_PROGRESS']
table_header = 'CFN Stack Name | Status | Details' + '\n' + '----------------------------------' + '\n'


# FUNCTIONS--------------------------------------------
# Define a substring that is included in the cfn stack names that you want to check the statuses of.
def get_stacks_to_be_tested():
	stacks_to_be_checked = []
	all_the_names = get_all_stack_names()
	for key in all_the_names:
		if "ForThePeople" in key:
			stacks_to_be_checked.append(key)
	return stacks_to_be_checked

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

# Checks if the user-input stack names actually exist in cfn, so compares against cfn reality
# Returns a boolean
def check_existence_of_stacks(stacks_to_be_checked):
	all_stacks_exist = True
	all_stacks_names = get_all_stack_names()
	for one_stack in stacks_to_be_checked:
		if one_stack not in all_stacks_names:
			all_stacks_exist = False
	return all_stacks_exist

# Returns a dict of all the stack statuses from the user-picked cfn stack names.
# ALL user-picked stack names must pass an existence check or else ALL will fail.
def get_status_using_stack_names(stacks_to_be_checked):
	all_stacks_exist = check_existence_of_stacks(stacks_to_be_checked)
	# list_of_stack_statuses = []
	dict_of_stack_statuses = {}
	if all_stacks_exist == True:
		response = get_all_stacks_info()
		for one_stack in stacks_to_be_checked:
			for key in response['StackSummaries']:
				if one_stack == key[stack_name] and stack_status in key:
					dict_of_stack_statuses[key[stack_name]] = key[stack_status]
	# 				list_of_stack_statuses.append(key[stack_status])
	# return list_of_stack_statuses
	return dict_of_stack_statuses

# Takes the raw dict of the cfn stack results and returns a string that is more human readable.
def manipulate_results_data_for_humans(raw_results):
	color = 'R'
	human_friendly_results = ""
	for i in raw_results:
		if raw_results[i] in success_states:
			color = 'G'
		elif raw_results[i] in in_progress_states:
			color = 'Y'
		else:
			color = 'R'
		# print i, color, results[i]
		human_friendly_results += i+" | "+color+" | "+raw_results[i] +'\n'
	return human_friendly_results

# Creates or replaces a file and writes results (recommended to use human readable results) to it. 
def write_results_to_file(results_from_cfn_stacks):
	with open("cfn-stack-results.md","a+") as file:
		file.truncate(0)
		file.write(table_header)
		file.write(results_from_cfn_stacks)
		file.close()

# THE VERSION USING STACK_ID instead of stack names
# Returns a list of cfn statuses based on the stack IDs
# The results of this data are not used in other functions.
# So this is basically OUT-OF-USE for now.
# DON'T USE THIS unless you have some special case. Stick with cfn names.
# Uncomment and change the string below to the stack id you want to check
# stack_id = ['']
def get_status_using_stack_ids(stack_id):
	resource = boto3.resource('cloudformation')
	list_of_status = []
	for one_id in stack_id:
		status = resource.Stack(one_id).stack_status
		list_of_status.append(status)
	return list_of_status


# TESTS-------------------------------------------------
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

def test_check_existence_of_stacks(stacks_to_be_checked):
	existence = check_existence_of_stacks(stacks_to_be_checked)
	print existence

def test_get_status_using_stack_names(stacks_to_be_checked):
	status_of_stacks = get_status_using_stack_names(stacks_to_be_checked)
	print status_of_stacks

# test_get_all_stacks_info()
# test_get_all_stack_names()
# test_get_status_using_stack_ids(stack_id)
# test_get_status_using_stack_names(stacks_to_be_checked)
# test_check_existence_of_stacks(stacks_to_be_checked)


# SCRIPT TO RUN PROGRAM-----------------------------------
# These four steps will get the stack names to be checked,
# Check the status of those specific cfn stacks,
# And output the results into a file named cfn-stack-results.md
stacks_to_be_checked = get_stacks_to_be_tested()
raw_results = get_status_using_stack_names(stacks_to_be_checked)
human_friendly_results = manipulate_results_data_for_humans(raw_results)
write_results_to_file(human_friendly_results)
