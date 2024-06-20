import datetime, json

from habit_app.models import Topic, Task, UserDefinedUnits

# calculating difference in 2 dates of string type
def calc_duration_days(startdate, enddate):
    start         = datetime.datetime.strptime(startdate, "%Y-%m-%d")
    end           = datetime.datetime.strptime(enddate, "%Y-%m-%d")
    difference    = end - start
    duration_days = difference.days
    return duration_days


# Add topic and task together along with user defined unit if provided
def insert_plan_data(plan, user):
    # Data for Topic
    try:
        user_id       = user
        topic_name    = plan.get('topicname')
        start_date    = plan.get('startdate')
        end_date      = plan.get('enddate')
        duration_days = calc_duration_days(start_date, end_date)

        topic = Topic.objects.create(
            user_id       = user_id,
            topic_name    = topic_name,
            start_date    = start_date,
            end_date      = end_date,
            duration_days = duration_days
            )
        topic.save()

        
        # Data for Task
        topic_id = Topic.objects.filter(user_id = user_id, topic_name = topic_name)[0]
        tasks    = plan.get('tasks')  

        for task in tasks:
            taskname            = task.get('taskname')
            times               = task.get('times')
            system_defined_unit = task.get('system_defined_unit') 
            user_defined_unit   = task.get('user_defined_unit')

            if system_defined_unit != None and user_defined_unit != None:
                raise Exception("Choose only one type of unit System Defined / UserDefined")
            elif user_defined_unit == None and system_defined_unit != None:
                add_task_with_system_defined_unit(
                user_id,
                topic_id,
                taskname,
                times,
                system_defined_unit
            )
            else:
                add_task_with_user_defined_unit(
                    user_id,
                    topic_id,
                    taskname,
                    times,
                    user_defined_unit
                )

                if is_in_userdefined_unit(user_id, user_defined_unit) == False:
                    add_user_defined_unit(user_id, user_defined_unit)
        return "Plan Successfully created"
    except Exception as e:        
        return str(e)
    

# function to add new Task
def add_new_task(task, user):
    user_id             = user
    topic_id            = task.get('topicid')
    taskname            = task.get('taskname')
    times               = task.get('times')
    system_defined_unit = task.get('system_defined_unit')
    user_defined_unit   = task.get('user_defined_unit')

    topic_instance = get_topic_instance_by_id(topic_id)

    try:
        if system_defined_unit != None and user_defined_unit != None:
            raise Exception('only single unit can be set!!!')
        elif system_defined_unit != None and user_defined_unit is None:
            add_task_with_system_defined_unit(
                user_id,
                topic_instance,
                taskname,
                times,
                system_defined_unit
            )
        else:
            add_task_with_user_defined_unit(
                user_id,
                topic_instance,
                taskname,
                times,
                user_defined_unit
            )
            
            if is_in_userdefined_unit(user_id, user_defined_unit) == False:
                add_user_defined_unit(user_id, user_defined_unit)
        return "success"
    except Exception as e:
        return str(e)


# Creating task with system designed records
def add_task_with_system_defined_unit(user_id, topic_id, taskname, times, system_defined_unit):
    new_task = Task.objects.create(
        user_id             = user_id,
        topic_id            = topic_id,
        taskname            = taskname,
        times               = times,
        system_defined_unit = system_defined_unit
    )
    new_task.save()


# creating task with user designed records
def add_task_with_user_defined_unit(user_id, topic_id, taskname, times, user_defined_unit):
    new_task = Task.objects.create(
        user_id             = user_id,
        topic_id            = topic_id,
        taskname            = taskname,
        times               = times,
        user_defined_unit   = user_defined_unit
    )
    new_task.save()


# creating user defined units
def add_user_defined_unit(user_id, unit):
    unit = UserDefinedUnits.objects.create(
        user_id = user_id,
        unit    = unit
    )
    unit.save()


# retrieve topic instance by id 
def get_topic_instance_by_id(topic_id):
    topic_instance = Topic.objects.filter(id = topic_id)[0]
    return topic_instance


# To check if provided unit is already in user defined unit
def is_in_userdefined_unit(user_id, user_defined_unit):
    user_unit = UserDefinedUnits.objects.filter(
        user_id = user_id,
        unit    = user_defined_unit
        ).count()
    
    if user_unit == 0:
        return False
    else:
        return True