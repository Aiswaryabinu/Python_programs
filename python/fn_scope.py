def scope_test():
    def do_local():
        test="local test"
        print("local test :"+test)
    def do_non_local():
        nonlocal test
        test="non local" #replacing the default value in test to the non local value 
    def do_global():
        global test
        test="global"
    test="default"
    do_local()
    print("calling local :"+test)
    do_non_local()
    print("calling non local :"+test)
    do_global()
    print("Calling global :"+test)
scope_test()
print("Calling global :"+test)
    