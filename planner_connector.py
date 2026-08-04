from action_manager import create_task





def convert_plan_to_tasks(plan):


    created = []



    for step in plan["steps"]:


        task = create_task(

            step,

            "normal"

        )


        created.append(
            task
        )



    return created
