

# 参考方法2：增加了日期类型判断
# def convert_obj_to_dicts(model_obj):
#     import inspect, types
#
#     object_array = []
#
#     for obj in model_obj:
#         #         obj.last_update_time = obj.last_update_time.isoformat()
#         #         obj.create_time = obj.create_time.isoformat()
#         # 获取到所有属性
#         field_names_list = obj._meta.get_all_field_names()
#         print
#         field_names_list
#         for fieldName in field_names_list:
#             try:
#                 fieldValue = getattr(obj, fieldName)  # 获取属性值
#                 print
#                 fieldName, "--", type(fieldValue), "--", hasattr(fieldValue, "__dict__")
#                 if type(fieldValue) is datetime.date or type(fieldValue) is datetime.datetime:
#                     #                     fieldValue = fieldValue.isoformat()
#                     fieldValue = datetime.datetime.strftime(fieldValue, '%Y-%m-%d %H:%M:%S')
#                     # 没想好外键与cache字段的解决办法
#                 #                 if hasattr(fieldValue, "__dict__"):
#                 #                     fieldValue = convert_obj_to_dicts(model_obj)
#
#                 setattr(obj, fieldName, fieldValue)
#             # print fieldName, "\t", fieldValue
#             except Exception, ex:
#                 print
#                 ex
#                 pass
#                 # 先把Object对象转换成Dict
#         dict = {}
#         dict.update(obj.__dict__)
#         dict.pop("_state", None)  # 此处删除了model对象多余的字段
#         object_array.append(dict)
#     print
#     object_array
#
#     return object_array
#
