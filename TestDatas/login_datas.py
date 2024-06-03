

#正常场景，测试用例
successs_data=[{'user':'qiaort','passwd':'2024@Set'}]


#异常场景
fali_data=[
    {'user':'sdfsd','passwd':'sfasd','check':'用户名或密码错误'},
    {'user':'','passwd':'sfasd','check':'用户名不能为空'},
    {'user':'sfas','passwd':'','check':'密码不能为空'}
]