from playwright.sync_api import sync_playwright     #文件名和文件夹名称不能重复,否则会导包失败.

def pw_test():
    pl = sync_playwright().start()    #实例化 sync_playwright
    browser = pl.chromium.launch(headless = False)     #浏览器内核firefox \chrome \ webkit
    context = browser.new_context()     #上下文
    page = context.new_page()
    page.goto("http://192.168.0.105")
    page.pause()     #会开启录屏模式
    page.wait_for_timeout(1000)        #类似于 sleep
