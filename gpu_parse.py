from amdsmi import *

try:
    amdsmi_init()
    num_of_GPUs = len(amdsmi_get_processor_handles())
    print("Number of GPUs ", num_of_GPUs)
    if num_of_GPUs > 0:
        handles = amdsmi_get_processor_handles()
        print("----------------------------")
        for i, handle in enumerate(handles):
            print(f"GPU number {i} details: ")
            type_of_GPU = amdsmi_get_processor_type(handle)
            print("amdsmi_get_processor_type ",type_of_GPU)
            device_id = amdsmi_get_gpu_device_uuid(handle)
            print("amdsmi_get_gpu_device_uuid ",device_id)
            driver_info = amdsmi_get_gpu_driver_info(handle)
            print("amdsmi_get_gpu_driver_info ", driver_info)
            
            print("----------------------------")

except AmdSmiException as e:
    print(e)
finally:
    try:
        amdsmi_shut_down()
    except AmdSmiException as e:
        print(e)