#Task and Lists
#Sara Hernandez
#November 20,2022
#Function that print "All items are ready" if character has picked all the items needed to perform a certain task

import random
taskList = ['Climb a mountain', 'Cook a meal', 'Write a book']
initial_conditions = ['pan','coat','idea','rope','groceries']
status_debuff = 'small'

character_task = random.choice(taskList)

item_list = []
def items_ready(task):
    if task == 'Climb a mountain' and 'rope' in initial_conditions and 'coat' in initial_conditions and 'first aid kits' in initial_conditions:
        task_status =  'All items are ready'
    elif task == 'Cook a meal' and 'pan' in initial_conditions and 'groceries' in initial_conditions:
        task_status =  'All items are ready'
    elif task == 'Write a book' and 'pen' in initial_conditions and 'paper' in initial_conditions and 'idea' in initial_conditions:
        task_status = 'All items are ready'
    else:
        task_status = 'Some items are missing'

    if task == 'Climb a mountain' and status_debuff == 'small':
        debuff_status = 'The task\'s debuff status has a negative impact on the game character.'
    else:
        debuff_status = 'The game character is not affected by the task\'s debuff status.'

    return task_status, debuff_status


items_ready_results = items_ready(character_task)
print('Character\'s random task was ' + '"' + character_task + '".', items_ready_results[0] + '.', items_ready_results[1])