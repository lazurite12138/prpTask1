#Python 概念总结
##基本数据类型
###不可变数据：数字、字符串、元组
###可变数据：列表、字典、集合
***
###[数字(Number)](https://www.runoob.com/python3/python3-number.html)
###只有3种数值类型：
* 整型(int)-即整数，不带小数点，布尔(bool)是其子类型。
* 浮点型(float)-即小数，也包括用科学计数法表示的数。
* 复数(complex)-即复数，用`complex(a,b)`表示，其中a,b都为float。

这一块较为简单，需要用到具体函数时可再搜索

相关函数可点击标题查看
***
###[字符串(String)](https://www.runoob.com/python3/python3-string.html)
* 可用`''`或`“”`来创建字符串

* 访问字符串中的值: 访问其中一个字符(形如`str[0]`，`str[-3]`)或访问其中一段(形如`str[0:]`,`str[:]`,`str[1:-2]`)。
【第1个字符为`str[0]`,对于负数,将其加上字符长度即为正常表达】

* 转义字符:只用特殊字符如\,"，换行时要用到。

* 字符串运算符:如连接，截取等。

* 字符串格式化:与C中sprintf一样语法。
***
###[元组(Tuple)](https://www.runoob.com/python3/python3-tuple.html)
* 与列表类似，但是元组的元素不能改(如果其元素是列表，则列表元素可以更改)

* 创建元组:`tup1=("a",1,2)`(不用括号也可以) (当创建元组时只有一个元素，需要在元素后加逗号)

* 访问元组中的值与字符串类似
***
###[列表(List)](https://www.runoob.com/python3/python3-list.html)
* 列表与C++中数组最相似，但也有所不同，其元素类型不必统一。

* 创建列表用`[   ]`

* 访问列表中的值与字符串类似

* 列表自带函数种类较多，如`append()`,`pop()`等，可以作栈或队列用
***
###[字典(Dictionary)](https://www.runoob.com/python3/python3-dictionary.html)
* 字典类似于一个函数,允许一对多，不允许多对一，其余和真的“字典”含义差不多

* 创建字典:`dict={1:"one",2:"two"}`,一个key对应一个value。

* 访问字典的值:`dict[1]`,`dict["Name"]` (注意用中括号)

* 内置函数可点击标题或直接搜
***
###[集合(Set)](https://www.runoob.com/python3/python3-set.html)
* 等价于数学概念中的集合,无序、无重复元素

* 创建集合:`seta={1,2,3}`,也可用`seta=("abcdsa")` (空集合必须用`set()`)

* 基本操作:`add()`,`remove()`等

* 集合间的运算

1. a-b a中有,b中没有的 
2. a|b 取并集
3. a&b 取交集
4. a^b 取交集对并集的补集
***
***
##函数与类
###main函数
* python作为一个解释型语言，不同于C++等编译型语言，对main函数的要求并不是必须的。但设置main函数可便于模块/函数的单独调试。

* 另外，对于`if _name_=="_main_":`语句包含的代码，只会在本模块单独运行时有效，若本模块被其他模块调用，则该代码不会执行。

###[函数](https://www.runoob.com/python3/python3-function.html)

* 定义函数的格式：
  
```
def func(参数列表):
    函数体(注意缩进)
    return(可有可无，若无则自动返回none)
```
* 传入函数的对象分为可变对象与不可变对象，对应数据类型中的可变数据类型与不可变数据类型(其实就是C++中的值传递与引用传递)

* 调用函数时正式参数类型有4种(也就是能否不写参数，能不能少写参数的问题)，具体可见标题。

* [匿名函数(python里即为lambda)](https://blog.csdn.net/Liveor_Die/article/details/78667075)

  * lambda函数经常用于简化代码(尤其是用于一些较为简单的，不在其他地方使用的函数的定义)
  * 格式:`lambda (参数列表):expression`
  * 既可以定义一个变量去接受lambda，也可直接将lambda当作一个变量
###[类](https://zhuanlan.zhihu.com/p/30024792)

* 与C++中的类格式与作用都相似
* 格式:
  ```
  class 类名():
    def __init__(self,参数列表):
        函数体
      
            ```
  

   
  
  
  