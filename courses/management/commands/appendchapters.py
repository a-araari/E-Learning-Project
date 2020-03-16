from django.core.management.base import BaseCommand
from courses.models import Course, Chapter
from users.models import Teacher
from random import randint


class Command(BaseCommand):

	chapter_names = [
		'Syntax',
		'Data Type',
		'Data Type Conversion',
		'Literals',
		'Expressions',
		'Conditions',
		'Blocks',
		'Classes',
		'Examples & Practice',
	]

	def handle(self, *args, **kwargs):
		course_list = Course.objects.all()

		for course in course_list:
			self.stdout.write(self.style.SUCCESS(f'Alter \'{course.name}\' course :'))
			max_iter = randint(2, len(self.chapter_names) - 1)
			count = 1
			for name in self.chapter_names:
				self.stdout.write(self.style.SUCCESS(f'	Creating \'{name}\' chapter..'))
				chapter, created = course.chapter_set.get_or_create(name=name)
				chapter.name = name
				chapter.detail = f'Get a good knowledge about {course.name} {name}'
				chapter.content = self.content.get(str(randint(0, 2)))
				chapter.course = course

				chapter.save() 
				self.stdout.write(self.style.SUCCESS(f'	\'{name}\' created/'))

				if count > max_iter:
					break
				count += 1

	content = {'1': """<h1><span style="color:#e74c3c"><strong>Decorators in ...</strong></span></h1>

<p>In <span style="color:#ffffff"><strong><span style="background-color:#000000">Python</span></strong></span>, functions are the first class objects, which means that &ndash;</p>

<ul>
	<li>Functions are objects; they can be referenced to, passed to a variable and returned from other functions as well.</li>
	<li>Functions can be defined inside another function and can also be passed as argument to another function.</li>
</ul>

<p><a href="https://www.geeksforgeeks.org/function-decorators-in-python-set-1-introduction/">Decorators</a>&nbsp;are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class. Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.</p>

<p><strong>Syntax for Decorators</strong></p>

<pre>
<code class="language-python">@gfg_decorator

def hello_decorator():

    print("Gfg")

'''Above code is equivalent to -

def hello_decorator():

    print("Gfg")

hello_decorator = gfg_decorator(hello_decorator)'''</code></pre>

<p>In the above code,&nbsp;<code>gfg_decorator</code>&nbsp;is a callable function, will add some code on the top of some another callable function,&nbsp;<code>hello_decorator&nbsp;</code>function and return the wrapper function.</p>

<p><strong>Decorator can modify the behavior:</strong></p>

<pre>
<code class="language-html">&lt;html&gt;
&lt;head&gt;
   &lt;title&gt; Boo &lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
   &lt;h1&gt;Header&lt;/h1&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>

<p><br />
<span style="white-space:pre-wrap">Hello, this is before function execution</span><strong>Output:</strong><img alt="" src="https://media.geeksforgeeks.org/wp-content/uploads/decorators_step2.png" style="float:right; height:363px; width:500px" /></p>

<pre>
This is inside the function !!
This is after function execution</pre>

<p>&nbsp;</p>

<p>Let&rsquo;s see the behavior of the above code how it runs step by step when the &ldquo;function_to_be_used&rdquo; is called.</p>

<p>&nbsp;</p>

<p>&nbsp;<br />
Let&rsquo;s jump to another example where we can easily find out&nbsp;<strong>the execution time of a function</strong>&nbsp;using a decorator.</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<pre>
<code class="language-python">@gfg_decorator

def hello_decorator():

    print("Gfg")

'''Above code is equivalent to -

def hello_decorator():

    print("Gfg")

hello_decorator = gfg_decorator(hello_decorator)'''</code></pre>

<p><span style="white-space:pre-wrap">3628800</span><strong>Output:</strong></p>

<pre>
Total time taken in :  factorial 2.0061802864074707</pre>

""",


'2': """<h1><span style="color:#e74c3c"><strong>Bla bla bla..</strong></span></h1>

<p>In <span style="color:#ffffff"><strong><span style="background-color:#000000">Python</span></strong></span>, functions are the first class objects, which means that &ndash;</p>

<ul>
	<li>Functions are objects; they can be referenced to, passed to a variable and returned from other functions as well.</li>
	<li>Functions can be defined inside another function and can also be passed as argument to another function.</li>
</ul>

<p><a href="https://www.geeksforgeeks.org/function-decorators-in-python-set-1-introduction/">Decorators</a>&nbsp;are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class. Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.</p>

<p><strong>Syntax for Decorators</strong></p>

<pre>
<code class="language-python">@gfg_decorator

def handle(self, *args, **kwargs):
		count = int(input(f'Courses count(max={len(self.courses_name)}): '))
		course_list = Course.objects.all()
		teacher_list = Teacher.objects.all()

		while count >= 0:
			name = self.courses_name[randint(0, len(self.courses_name) - 1)]
	
			if (not Course.objects.filter(name=name).exists()):
				self.stdout.write(self.style.SUCCESS(f'Creating \'{name}\' course..'))
				course = Course()
				course.name = name
				course.detail = f'Learning {name} in short period and become a developer'
				# thum = self.get_thumbnail(name)
				# course.tumbnail = ImageFile(open(thum, "rb"))

				course.teacher = teacher_list[randint(0, teacher_list.count() - 1)]

				course.save() 
				self.stdout.write(self.style.SUCCESS(f'\'{name}\' created/'))
			count -= 1</code></pre>

<p>In the above code,&nbsp;<code>gfg_decorator</code>&nbsp;is a callable function, will add some code on the top of some another callable function,&nbsp;<code>hello_decorator&nbsp;</code>function and return the wrapper function.</p>

<p><strong>Decorator can modify the behavior:</strong></p>

<pre>
<code class="language-html">&lt;html&gt;
&lt;head&gt;
   &lt;title&gt; Boo &lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
   &lt;h1&gt;Header&lt;/h1&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>
<p><span style="white-space:pre-wrap">3628800</span><strong>Output:</strong></p>

<pre>
Total time taken in :  factorial 2.0061802864074707</pre>

""",
'3': """<h1><span style="color:#e74c3c"><strong>Bla bla bla..</strong></span></h1>

<p>In <span style="color:#ffffff"><strong><span style="background-color:#000000">Python</span></strong></span>, functions are the first class objects, which means that &ndash;</p>

<p>In the above code,&nbsp;<code>gfg_decorator</code>&nbsp;is a callable function, will add some code on the top of some another callable function,&nbsp;<code>hello_decorator&nbsp;</code>function and return the wrapper function.</p>

<p><strong>Decorator can modify the behavior:</strong></p>

<pre>
<code class="language-html">&lt;html&gt;
&lt;head&gt;
   &lt;title&gt; Boo &lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
   &lt;h1&gt;Header&lt;/h1&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>
<p><span style="white-space:pre-wrap">3628800</span><strong>Output:</strong></p>

<pre>
Total time taken in :  factorial 2.0061802864074707</pre>
<ul>
	<li>Functions are objects; they can be referenced to, passed to a variable and returned from other functions as well.</li>
	<li>Functions can be defined inside another function and can also be passed as argument to another function.</li>
</ul>

<p><a href="https://www.geeksforgeeks.org/function-decorators-in-python-set-1-introduction/">Decorators</a>&nbsp;are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class. Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.</p>

<p><strong>Syntax for Decorators</strong></p>

<pre>
<code class="language-python">@gfg_decorator

def handle(self, *args, **kwargs):
		count = int(input(f'Courses count(max={len(self.courses_name)}): '))
		course_list = Course.objects.all()
		teacher_list = Teacher.objects.all()

		while count >= 0:
			name = self.courses_name[randint(0, len(self.courses_name) - 1)]
	
			if (not Course.objects.filter(name=name).exists()):
				self.stdout.write(self.style.SUCCESS(f'Creating \'{name}\' course..'))
				course = Course()
				course.name = name
				course.detail = f'Learning {name} in short period and become a developer'
				# thum = self.get_thumbnail(name)
				# course.tumbnail = ImageFile(open(thum, "rb"))

				course.teacher = teacher_list[randint(0, teacher_list.count() - 1)]

				course.save() 
				self.stdout.write(self.style.SUCCESS(f'\'{name}\' created/'))
			count -= 1</code></pre>


"""}