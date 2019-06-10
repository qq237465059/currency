from distutils.core import setup

setup(
    name='currencyReptile',
    version='1.0',
    author='hy',
    author_email='237465059@qq.com',
    description='可以自定义规则的爬虫',
    py_modules=['crawling.main'],
    packages=['crawling', 'crawling.config', 'crawling.regulation', 'crawling.databases', 'crawling.baseSpider', 'crawling.utils', 'crawling.output'],
    package_data={'': ['config.conf']}
)