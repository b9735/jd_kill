from selenium import webdriver

from utils.cookieUtil import checkCookie, mainPath, jobName
from selenium.webdriver.chrome.service import Service as ChromeService # Similar thing for firefox also!
from subprocess import CREATE_NO_WINDOW # This flag will only be available in windows



class ChromeBrowser:
    def __init__(self):
        chrome_options=self.prepareChrome()
        chrome_service = ChromeService(mainPath + "/driver/chromedriver.exe")
        chrome_service.creationflags=CREATE_NO_WINDOW
        # 告诉编译器chromedriver在哪个位置并注册(如更换驱动版本则需要进行修改)
        self.chrome = webdriver.Chrome(mainPath + "/driver/chromedriver.exe",
                                       chrome_options=chrome_options,service=chrome_service)

        # 设置窗口大小和位置
        self.chrome.set_window_size(390, 884)
        self.chrome.set_window_position(0, 0)

        # def openChrome(chrome_options):
        #     chrome = webdriver.Chrome(mainPath + "/utils/chromedriver",chrome_options=chrome_options)
        #     chrome.set_window_size(390, 884)
        #     chrome.set_window_position(0, 0)
    def prepareChrome(self):
        # 设置Chrome浏览器
        chrome_options = webdriver.ChromeOptions()
        # 设置UA
        chrome_options.add_argument(
            '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1')
        # 选择让谷歌模拟的设备
        # mobileEmulation = {"deviceName": "iPhone XR"}
        # chrome_options.add_experimental_option("mobileEmulation", mobileEmulation)

        # chrome_options.page_load_strategy = 'none'

        if checkCookie(jobName):
            # 隐身访问
            chrome_options.add_argument('--incognito')
            # 不加载图片, 提升速度
            chrome_options.add_argument('--blink-settings=imagesEnabled=false')
            # 不打开浏览器窗口
            chrome_options.add_argument("headless")
            # 修改加载策略为eager：等待初始HTML文档完全加载和解析，并放弃css、图像和子框架的加载。
            # chrome_options.page_load_strategy='eager'

        # chrome_options.add_argument("headless")
        # 隐藏正受到自动测试软件的控制。
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])


        return chrome_options