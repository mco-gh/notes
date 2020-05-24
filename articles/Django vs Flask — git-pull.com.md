Django vs Flask — git-pull.com

# Django vs Flask[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#django-vs-flask)

## A practitioner’s perspective[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#a-practitioner-s-perspective)

*June 2017*

This analysis is a comparison of 2 python web frameworks, Flask and Django. It discusses their features and how their technical philosophies impact software developers. It is based on my experience using both, as well as time spent personally admiring both codebases.

## Synopsis[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#synopsis)

Django is best suited for RDBMS-backed websites. Flask is good for corner cases that wouldn’t benefit from Django’s deep integration with RDBMS.

When using Flask, it’s easy to miss the comforts a full-fledge framework provides. Django’s extension community is more active. Django’s ORM is superb. Flask developers will be forced to reinvent the wheel to catch up for things that’d be quick wins with Django.

Both excel at prototyping; getting an idea off the ground fast, and leave room for chiseling away fine-grain details after. Python makes both a joy to work with.

## Concepts present in both frameworks[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#concepts-present-in-both-frameworks)

### Request object[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#request-object)

Information of user’s client request to server

[` flask.Request `](http://flask.pocoo.org/docs/api/#flask.Request) and [` django.http.HttpRequest `](http://docs.djangoproject.com/en/1.11/ref/request-response/#django.http.HttpRequest)

### URL routing[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#url-routing)

Routes HTTP requests (GET, POST, PUT, UPDATE), data payload, and URL path

[Django’s routing](http://docs.djangoproject.com/en/1.11/topics/http/urls/) and [Flask’s routing](http://flask.pocoo.org/docs/api/#url-route-registrations)

### Views[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#views)

Invoked when a request matches URL pattern and receives request object

[Django’s views](http://docs.djangoproject.com/en/1.11/topics/http/views/) and [Flask’s views](http://flask.pocoo.org/docs/views/#views)

Class-based: [django](http://docs.djangoproject.com/en/1.11/topics/class-based-views/) and[flask](http://flask.pocoo.org/docs/0.12/api/#class-based-views)

### Context information[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#context-information)

Passed into HTML template for processing.

[` django.template.Template.render() `](http://docs.djangoproject.com/en/1.11/ref/templates/api/#django.template.Template.render) (pass [` dict `](https://docs.python.org/2/library/stdtypes.html#dict) into[` Context `](http://docs.djangoproject.com/en/1.11/ref/templates/api/#django.template.Context) object)

[` flask.render_template() `](http://flask.pocoo.org/docs/api/#flask.render_template) (accepts [` dict `](https://docs.python.org/2/library/stdtypes.html#dict))

### HTML template engine[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#html-template-engine)

Renders template via context information.

[Django’s templating](http://docs.djangoproject.com/en/1.11/ref/templates/) and [Flask’s templating](http://flask.pocoo.org/docs/templating/)

### Response object[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#response-object)

Object with HTTP meta information and content to send to the browser.

[` django.http.HttpResponse `](http://docs.djangoproject.com/en/1.11/ref/request-response/#django.http.HttpResponse) and [` flask.Response `](http://flask.pocoo.org/docs/api/#flask.Response)

### Static file-handling[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#static-file-handling)

Handles static files like CSS, JS assets, and downloads.

[Static files in django](http://docs.djangoproject.com/en/1.11/howto/static-files/) and[Static files in Flask](http://flask.pocoo.org/docs/0.12/quickstart/#static-files)

## Django[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#django)

Today, Django is built and maintained by the open source community. The initial release was July 21, 2005, by Lawrence Journal-World.

### What Django provides[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#what-django-provides)

- [Template Engine](http://docs.djangoproject.com/en/1.11/ref/templates/)
    - [Filters](http://jinja.pocoo.org/docs/dev/templates/#filters)
    - [Tags](http://sphinx.readthedocs.io/en/latest/markup/misc.html#tags)
    - [Context preprocessor middleware](http://docs.djangoproject.com/en/1.11/ref/templates/api/#subclassing-context-requestcontext)(global, per-request [` dict `](https://docs.python.org/2/library/stdtypes.html#dict) passed into templates)
- [ORM](http://docs.djangoproject.com/en/1.11/topics/db/models/)
    - [` QuerySet `](http://docs.djangoproject.com/en/1.11/ref/models/querysets/#django.db.models.query.QuerySet) (reuseable object used in ORM-backed features)
    - [Migrations](http://docs.djangoproject.com/en/1.11/topics/migrations/)
    - [Raw Queries](http://docs.djangoproject.com/en/1.11/topics/db/sql/)
- [Forms](http://docs.djangoproject.com/en/1.11/topics/forms/)
    - [Fields](http://docs.djangoproject.com/en/1.11/ref/forms/fields/)
    - [Widgets](http://docs.djangoproject.com/en/1.11/ref/forms/widgets/)
    - [Model Forms](http://docs.djangoproject.com/en/1.11/topics/forms/modelforms/) (ORM-backed forms)
- [Views](http://docs.djangoproject.com/en/1.11/topics/http/views/)
    - [Class-based views](http://docs.djangoproject.com/en/1.11/topics/class-based-views/)
        - [` DetailView `](http://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView),[` ListView `](http://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-display/#django.views.generic.list.ListView) (ORM-backed views)
- [URL routing](http://docs.djangoproject.com/en/1.11/topics/http/urls/)
- [Administration web interface](http://docs.djangoproject.com/en/1.11/ref/contrib/admin/)(ORM-backed CRUD backend)
- [Authentication](http://docs.djangoproject.com/en/1.11/topics/auth/)
    - [` User `](http://docs.djangoproject.com/en/1.11/ref/contrib/auth/#django.contrib.auth.models.User) model
    - [Basic permission systems](http://docs.djangoproject.com/en/1.11/topics/auth/default/#topic-authorization)
- [Caching](http://docs.djangoproject.com/en/1.11/topics/cache/)
- [Multi-tenancy](http://docs.djangoproject.com/en/1.11/ref/contrib/sites/) via domain
- [Modularity via Apps](http://docs.djangoproject.com/en/1.11/ref/applications/)
- [Settings](http://docs.djangoproject.com/en/1.11/topics/settings/), configurable via [` DJANGO_SETTINGS_MODULE `](http://docs.djangoproject.com/en/1.11/topics/settings/#envvar-DJANGO_SETTINGS_MODULE)
- [Command system](http://docs.djangoproject.com/en/1.11/ref/django-admin/)
    - Shell with automatic integration of [bpython](https://bpython-interpreter.org/) and [ipython](https://ipython.org/), if detected
    - Launch DB command-line client (psql, mysql, sqlite3, sqlplus) based on engine configuration in settings.
    - [Custom commands](http://docs.djangoproject.com/en/1.11/howto/custom-management-commands/)
- [Static file support](http://docs.djangoproject.com/en/1.11/howto/static-files/)

### Extending Django[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#extending-django)

Django has a vibrant third-party development community. Apps are installed via appending them to the ` INSTALLED_APPS ` in the settings.

Popular Django extensions include:

- REST: [Django REST Framework](http://www.django-rest-framework.org/), aka “DRF”
- Permissions: [django-guardian](https://django-guardian.readthedocs.io/)
- Asset pipelines: [django-compressor](https://django-compressor.readthedocs.io/), [django-webpack-loader](https://github.com/ezhome/django-webpack-loader)
- Debugging, Miscellaneous: [django-extensions](https://django-extensions.readthedocs.io/), [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/)
- Filtering / Search: [django-filter](https://django-filter.readthedocs.io/)
- Tabular / paginated output of db: [django-tables2](https://django-tables2.readthedocs.io/)

Django extension project names tend to be prefixed *django-* and lowercase.

### Customizing Django[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#customizing-django)

Eventually the included forms, fields and class-based views included in Django aren’t going to be enough.

### Django’s scope[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#django-s-scope)

Django is a framework. The aspects django occupies are:

- mapping [database schemas](http://docs.djangoproject.com/en/1.11/topics/db/models/), [their queries](http://docs.djangoproject.com/en/1.11/topics/db/queries/), and [query results](http://docs.djangoproject.com/en/1.11/topics/db/queries/#retrieving-objects) to objects
- mapping [URL patterns](http://docs.djangoproject.com/en/1.11/topics/http/urls/) to [views](http://docs.djangoproject.com/en/1.11/topics/http/views/) containing business logic
- providing [request information](http://docs.djangoproject.com/en/1.11/ref/request-response/) such as GET, PUT, and [session stuff to views](https://docs.djangoproject.com/en/1.11/topics/http/sessions/#using-sessions-in-views)([` HttpRequest `](http://docs.djangoproject.com/en/1.11/ref/request-response/#django.http.HttpRequest))
- presenting data, including HTML [templates](http://docs.djangoproject.com/en/1.11/topics/templates/) and[JSON](http://docs.djangoproject.com/en/1.11/topics/serialization/#serialization-formats-json) ([` HttpResponse `](http://docs.djangoproject.com/en/1.11/ref/request-response/#django.http.HttpResponse))
- [environmental configuration](http://docs.djangoproject.com/en/1.11/topics/settings/) (settings) and an environment variables ([` DJANGO_SETTINGS_MODULE `](http://docs.djangoproject.com/en/1.11/topics/settings/#envvar-DJANGO_SETTINGS_MODULE)) e.g. dev, staging, prod workflows

A tool kit of libraries that abstract the monotony of common tasks in web projects.

If it’s difficult to visualize a web app in terms of its database schema and WordPress or Drupal would suffice, Django may not be the strongest pick for that.

Where a CMS will automatically provide a web admin to post content, toggle plugins and settings, and even allow user registration and comments, Django leaves you building blocks of components you customize to the situation. Programming is required.

Django’s programming language, python, also gives it a big boost.

#### Django uses classes right[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#django-uses-classes-right)

While python isn’t statically typed, its inheritance hierarchy is very straight-forward and navigable.

Code Editors:

Free tools in the community such as [jedi](http://jedi.readthedocs.io/) provide navigation of modules, functions and classes to editors like [vim](http://www.vim.org/), [Visual Studio Code](https://code.visualstudio.com/) and[Atom](https://atom.io/).

[Python classes](https://docs.python.org/2/tutorial/classes.html#tut-classes) benefit from many real-world examples being available in the open source community to study. They’re a pleasure incorporating in your code. An example for django would be [class-based views](http://docs.djangoproject.com/en/1.11/topics/class-based-views/)which shipped in [Django 1.3](http://docs.djangoproject.com/en/1.11/releases/1.3/).

OOP + Python:

For those seeking a good example of OOP in Python, in addition to class-based views, Django is a sweeping resource. It abstracts out HTTP requests and responses, as well as SQL dialects in a class hierarchy.

See my answer on HN for *Ask HN: How often do you use inheritance?*:https://news.ycombinator.com/item?id=14329256

#### Stretching the batteries[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#stretching-the-batteries)

Django isn’t preventing custom solutions. It provides a couple of frameworks which complement each other and handles initializing the frameworks being used via project’s settings. If a project doesn’t leverage a component Django provides, it stays out of the way.

Let’s try a few examples of how flexible Django is.
**Scenario 1:** Displaying a user profile on a website.
URL pattern is ` r"^profile/(?P<pk>\d+)/$" `, e.g. */profile/1*

Let’s begin by using the simplest view possible, and map directly to a function, grab the user model via [` get_user_model() `](http://docs.djangoproject.com/en/1.11/topics/auth/customizing/#django.contrib.auth.get_user_model):

from  django.contrib.auth  import  get_user_modelfrom  django.http  import  HttpResponsedef  user_profile(request,  **kwargs):  User  =  get_user_model()  user  =  User.objects.get(pk=kwargs['pk'])  html  =  "<html><body>Full Name: *%s*.</body></html>"  %  user.get_full_name()  return  HttpResponse(html)

*urls.py*:

from  django.conf.urls  import  urlfrom  .views  import  user_profileurlpatterns  =  [  url(r'^profile/(?P<pk>\d+)/$',  user_profile),]

So where does the ` request, **kwargs ` in ` user_profile ` come from? Django injects the user’s request and any URL group pattern matches to views when the user visits a page matching a URL pattern.

1. [` HttpRequest `](http://docs.djangoproject.com/en/1.11/ref/request-response/#django.http.HttpRequest) is passed into the view as ` request `.

2. Since the URL pattern, ` r'^profile/(?P<pk>\d+)/$' `, contains a named group,` pk `, that will be passed via [Keyword Arguments](https://docs.python.org/2/tutorial/controlflow.html#tut-keywordargs)  ` **kwargs `.

If it was ` r'^profile/(\d+)/$' `, it’d be passed in as [` tuple() `](https://docs.python.org/2/library/functions.html#tuple)argument into the ` *arg ` parameter.

Arguments and Parameters:

Learn [the difference between arguments and parameters](https://docs.python.org/2/faq/programming.html#faq-argument-vs-parameter).

**Bring in a high-level view:**

Django has an opinionated flow and a shortcut for this. By using the named regular expression group ` pk `, there is a class that will automatically return an object for that key.

So, it looks like a [` DetailView `](http://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView) is best suited. We only want to get information on one core object.

Easy enough, [` get_object() `](http://docs.djangoproject.com/en/1.11/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_object)’s default behavior grabs the PK:

from  django.contrib.auth  import  get_user_modelfrom  django.views.generic.detail  import  DetailViewclass  UserProfile(DetailView):  model  =  get_user_model()

*urls.py*:

from  django.conf.urls  import  urlfrom  .views  import  UserProfileurlpatterns  =  [  url(r'^profile/(?P<pk>\d+)/$',  UserProfile.as_view()),]

Append [` as_view() `](http://docs.djangoproject.com/en/1.11/ref/class-based-views/base/#django.views.generic.base.View.as_view) to routes using class-based views.

If *profile/1* is missing a template, accessing the page displays an error:
django.template.exceptions.TemplateDoesNotExist:  core/myuser_detail.html

The file location and name depends on the app name and model name. Create a new template in the location after [` TemplateDoesNotExist `](http://docs.djangoproject.com/en/1.11/topics/templates/#django.template.TemplateDoesNotExist)in any of the projects *templates/* directories.

In this circumstance, it needs *core/myuser_detail.html*. Let’s use the app’s template directory. So inside *core/templates/core/myuser_detail.html*, make a file with this HTML:

<html><body>Full name: {{ object.get_full_name }}</body></html>

Custom template paths can be specified via punching out[` template_name `](http://docs.djangoproject.com/en/1.11/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_name)in the view.

That works in any descendent of [` TemplateView `](http://docs.djangoproject.com/en/1.11/ref/class-based-views/base/#django.views.generic.base.TemplateView)or class mixing in [` TemplateResponseMixin `](http://docs.djangoproject.com/en/1.11/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin).

Note:

Django doesn’t require using [` DetailView `](http://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView).

A plain-old [` View `](http://docs.djangoproject.com/en/1.11/ref/class-based-views/base/#django.views.generic.base.View) could work. Or a [` TemplateView `](http://docs.djangoproject.com/en/1.11/ref/class-based-views/base/#django.views.generic.base.TemplateView) if there’s an HTML template.

As seen above, there are [function views](http://docs.djangoproject.com/en/1.11/topics/http/views/).

These creature comforts were put into Django because they represent bread and butter cases. It makes additional sense when factoring in[REST](https://en.wikipedia.org/wiki/Representational_state_transfer).

**Harder:** Getting the user by a username

Next, let’s try usernames instead of user ID’s, */profile/yourusername*. In the views file:

from  django.contrib.auth  import  get_user_modelfrom  django.http  import  HttpResponsedef  user_profile(request,  **kwargs):  User  =  get_user_model()  user  =  User.objects.get(username=kwargs['username'])  html  =  "<html><body>Full Name: *%s*.</body></html>"  %  user.get_full_name()  return  HttpResponse(html)

*urls.py*:

from  django.conf.urls  import  urlfrom  .views  import  user_profileurlpatterns  =  [  url(r'^profile/(?P<pk>\w+)/$',  user_profile),]

Notice how we switched the regex to use ` \w ` for alphanumeric character and the underscore. Equivalent to ` [a-zA-Z0-9_] `.

For the class-based view, the template stays the same. View has an addition:

class  UserProfile(DetailView):  model  =  get_user_model()  slug_field  =  'username'

*urls.py*:
urlpatterns  =  [  url(r'^profile/(?P<slug>\w+)/$',  UserProfile.as_view()),]

Another “shortcut” ` DetailView ` provides; a *slug*. It’s derived from[` SingleObjectMixin `](http://docs.djangoproject.com/en/1.11/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin). Since the url pattern has a named group, i.e. ` (?P<slug>\w+) ` as opposed to ` (\w+) `.

But, let’s say the named group “slug” doesn’t convey enough meaning. We want to be accurate to what it is, a *username*:

urlpatterns  =  [  url(r'^profile/(?P<username>\w+)/$',  UserProfile.as_view()),]

We can specify a [` slug_url_kwarg `](http://docs.djangoproject.com/en/1.11/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.slug_url_kwarg):

class  UserProfile(DetailView):  model  =  get_user_model()  slug_field  =  'username'  slug_url_kwarg  =  'username'

**Make it trickier:** User’s logged in profile
If a user is logged in, */profile* should take them to their user page.
So a pattern of ` r"^profile/$" `, in *urls.py*:
urlpatterns  =  [  url(r'^profile/$',  UserProfile.as_view()),]

Since there’s no way to pull up the user’s ID from the URL, we need to pull their authentication info to get that profile.

Django thought about that. Django can attach the user’s information to the[` HttpRequest `](http://docs.djangoproject.com/en/1.11/ref/request-response/#django.http.HttpRequest) so the view can use it. Via[` user `](http://docs.djangoproject.com/en/1.11/ref/request-response/#django.http.HttpRequest.user).

In the project’s [settings](http://docs.djangoproject.com/en/1.11/topics/settings/), add[` AuthenticationMiddleware `](http://docs.djangoproject.com/en/1.11/ref/middleware/#django.contrib.auth.middleware.AuthenticationMiddleware) to` MIDDLEWARE `:

MIDDLEWARE  =  [  *# ... other middleware*  'django.contrib.auth.middleware.AuthenticationMiddleware',]

In the view file, using the same template:

class  UserProfile(DetailView):  def  get_object(self):  return  self.request.user

This overrides [` get_object() `](http://docs.djangoproject.com/en/1.11/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_object)to pull the [` User `](http://docs.djangoproject.com/en/1.11/ref/contrib/auth/#django.contrib.auth.models.User) right out of the request.

This page only will work if logged in, so let’s use[` login_required() `](http://docs.djangoproject.com/en/1.11/topics/auth/default/#django.contrib.auth.decorators.login_required), in*urls.py*:

from  django.contrib.auth.decorators  import  login_requiredurlpatterns  =  [  url(r'^profile/$',  login_required(UserProfile.as_view())),]

That will assure only logged-in users can view the page. It will also send the user to a login form which forward them back to the page after login.

Even with high-level reuseable components, there’s a lot of versatility and tweaking oppurtunities. This saves time from hacking up solution for common cases. Reducing bugs, making code uniform, and freeing up time for the stuff that will be more specialized.

#### Retrofit the batteries[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#retrofit-the-batteries)

Relying on the django’s components, such as views and forms, gives developers certainty things will behave with certainty. When customizations needs to happen, it’s helpful to see if [subclassing a widget](http://docs.djangoproject.com/en/1.11/ref/forms/widgets/#base-widget-classes)or [form field](http://docs.djangoproject.com/en/1.11/ref/forms/fields/) would do the trick. This assures the new custom components gets the validation, form state-awareness, and template output of the form framework.

### Configuring Django[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#configuring-django)

Django’s [settings](http://docs.djangoproject.com/en/1.11/topics/settings/) are stored in a python file. This means that the Django configuration can include any python code, including accessing environment variables, importing other modules, checking if a file exists, lists, tuples, arrays, and dicts.

Django relies on an [environment variable](https://en.wikipedia.org/wiki/Environment_variable), [` DJANGO_SETTINGS_MODULE `](http://docs.djangoproject.com/en/1.11/topics/settings/#envvar-DJANGO_SETTINGS_MODULE), to load a module of setting information.

Settings are a [lazily-loaded](https://en.wikipedia.org/wiki/Lazy_initialization)[singleton](https://en.wikipedia.org/wiki/Singleton_pattern) object:

- > When an > [> attribute](https://docs.python.org/2/tutorial/classes.html#tut-classobjects)>  of ` django.conf.settings `> is accessed, it will do a onetime “setup”. The section > [> Django’s intialization](https://www.git-pull.com/code_explorer/django-vs-flask.html#djangos-initialization)> shows there’s a few ways settings get configured.
- *> Singleton*> , meaning that it can be imported from throughout the application code and still retrieve the same instance of the object.

> Reminder> :

> Sometimes global interpreter locks and thread safety are brought up when discussing languages. Web admin interfaces and JSON API’s aren’t CPU bound. Most web problems are I/O bound.

> In other words, issues websites face when scaling are concurrency related. In practice, it’s not even limited to the dichotomy of concurrency and parallelism: Websites scale by offloading to infrastructure such as > [> reverse proxies](https://en.wikipedia.org/wiki/Reverse_proxy)> , task queues (e.g. > [> Celery](http://www.celeryproject.org/)> ,> [> RQ](http://python-rq.org/)> ), and > [> replicated databases](https://en.wikipedia.org/wiki/Replication_(computing)#DATABASE)> . Computational heavy backend services are done elsewhere and use different tools (kafka, hadoop, spark, Elasticsearch, etc).

Django uses [` import_module() `](https://docs.python.org/2/library/importlib.html#importlib.import_module) to turn a string into a[module](https://docs.python.org/2/tutorial/modules.html#tut-modules). It’s kind of like an ` eval `, but strictly for importing. [It happens here](https://github.com/django/django/blob/1.11.2/django/conf/__init__.py#L110).

It’s available as an environmental variable as projects commonly have multiple settings files. For instance, a base settings file, then other files for[local, development, staging, and production](https://en.wikipedia.org/wiki/Deployment_environment). Those 3 will have different database configurations. Production will likely have heavy caching.

To access settings attributes application-wide, import the settings:
from  django.conf  import  settings
From there, attributes can be accessed:
print(settings.DATABASES)
Virtual environments and site packages:

When developing via a shell, not being sourced into a virtual enviroment could lead to a settings module (and probably the django package itself) not being found.

The same applies to UWSGI configurations, similar symptoms will arise when deploying. This can be done via the ` virtualenv ` option.

This is the single biggest learning barrier python has. It will be a hindrance every step of the way until the concept is internalized.

### Django’s intialization[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#django-s-intialization)

Django’s initialization is complicated. However, its complexity is proportional to what’s required to do the job.

As seen in [Configuring Django](https://www.git-pull.com/code_explorer/django-vs-flask.html#configuring-django), the settings are loaded as a side-effect of accessing the setting object.

In addition to that, django maintains an application registry, [` apps `](http://docs.djangoproject.com/en/1.11/ref/applications/#django.apps.apps), also a singleton. It’s populated via [` django.setup() `](http://docs.djangoproject.com/en/1.11/ref/applications/#django.setup).

Finding and loading the settings requires an environmental variable is set. Django’s generated manage.py will set a default one if its unspecified.

#### via command-line / manage.py (development)[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#via-command-line-manage-py-development)

1. User runs ` ./manage.py ` (including arguments, e.g. 	 ./manage.py

	collectstatic

2. ` settings ` are [lazily loaded](https://github.com/django/django/blob/1.11.2/django/conf/__init__.py#L201) upon import of` execute_from_command_line ` of ` django.core.management `.

[Accessing an attribute](https://github.com/django/django/blob/1.11.2/django/conf/__init__.py#L51) of ` settings ` (e.g. ` if settings.configured `) implicitly imports the settings module’s information.

3. ` execute_from_command_line() ` accepts [` sys.argv `](https://docs.python.org/2/library/sys.html#sys.argv) and passes them to initialize [ManagementUtility](https://github.com/django/django/blob/1.11.2/django/core/management/__init__.py#L133)

4. ` ManagementUtility.execute() ` ([source](https://github.com/django/django/blob/1.11.2/django/core/management/__init__.py#L284)) pulls a settings attribute for the first time, invokes[` django.setup() `](http://docs.djangoproject.com/en/1.11/ref/applications/#django.setup) (populating the app registry)

5. ` ManagementUtility.execute() ` directs ` sys.argv ` command to the appropriate app functions. A list of commands [are cached](https://github.com/django/django/blob/1.11.2/django/core/management/__init__.py#L44). In addition, these are hard-coded:

    - autocompletion
    - ` runserver `
    - help output (` --help `)

In addition, upon running, commands will run [system checks](http://docs.djangoproject.com/en/1.11/topics/checks/) (since [Django 1.7](http://docs.djangoproject.com/en/1.11/releases/1.7/)). Any command inheriting from [` BaseCommand `](http://docs.djangoproject.com/en/1.11/howto/custom-management-commands/#django.core.management.BaseCommand)runs checks implicitly. ` ./manage.py check ` will run checks explicitly.

#### via WSGI (server)[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#via-wsgi-server)

1. Point WSGI server wrapper (e.g. UWSGI) [to wsgi.py generated by Django](http://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/)

2. uwsgi.py will run [get_wsgi_application()](https://github.com/django/django/blob/1.11.2/django/core/wsgi.py#L5)

3. [` django.setup() `](http://docs.djangoproject.com/en/1.11/ref/applications/#django.setup)

4. Serves WSGI-compatible response

## Flask[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#id4)

Flask is also built and maintained in the open source community. The project, as well as its dependencies, [Jinja2](http://jinja.pocoo.org/) and [Werkzeug](http://werkzeug.pocoo.org/), are [Pallets projects](https://www.palletsprojects.com/). The creator of the software itself is Armin Ronacher. Initial release April 1, 2010.

### What Flask provides[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#what-flask-provides)

- [Template system](http://flask.pocoo.org/docs/templating/) via [Jinja2](http://jinja.pocoo.org/)
- [URL routing](http://flask.pocoo.org/docs/api/#url-route-registrations) via [Werkzeug](http://werkzeug.pocoo.org/)
- Modularity via [blueprints](http://flask.pocoo.org/docs/blueprints/#blueprints)
- In-browser REPL-powered tracebook debugging via Werkzeug’s
- Static file handling

### Extending Flask[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#extending-flask)

Since Flask doesn’t include things like an ORM, authentication and access control, it’s up to the user to include libraries to handle those a la carte.

Popular Flask extensions include:

- Database: [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/)
- REST: [Flask-RESTful](https://flask-restful.readthedocs.io/) ([flask-restful-swagger](https://github.com/rantav/flask-restful-swagger)), [Flask API](http://www.flaskapi.org/)
- Admins: [Flask-Admin](https://github.com/flask-admin/flask-admin)  [Flask-SuperAdmin](https://github.com/SyrusAkbary/Flask-SuperAdmin)
- Auth: [Flask-Login](https://flask-login.readthedocs.io/), [Flask-Security](https://flask-security.readthedocs.io/)
- Asset Pipeline: [Flask-Assets](https://flask-assets.readthedocs.io/), [Flask-Webpack](https://github.com/nickjj/flask-webpack)
- Commands: [Flask-Script](https://flask-script.readthedocs.io/)

Flask extension project names tend to be prefixed *Flask-*, [PascalCase](https://en.wikipedia.org/wiki/PascalCase), with the first letter of words uppercase.

Used with flask, but not flask-specific (could be used in normal scripts):

- Social authentication: [authomatic](https://github.com/authomatic/authomatic), [python-social-auth](https://github.com/omab/python-social-auth)
- Forms: [WTForms](https://wtforms.readthedocs.io/)
- RDBMS: [SQLAlchemy](https://sqlalchemy.org/), [peewee](http://docs.peewee-orm.com/)
- Mongo: [MongoEngine](http://docs.mongoengine.org/)

For more, see [awesome-flask](https://github.com/humiaozuzu/awesome-flask) on github.

### Configuring Flask[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#configuring-flask)

Configuration is typically added after [` Flask `](http://flask.pocoo.org/docs/api/#flask.Flask)*object* is initialized. No server is running at this point:

app  =  Flask(__name__)

After initialization, configuration available via a [` dict `](https://docs.python.org/2/library/stdtypes.html#dict)-like attribute via the [` Flask.config `](http://flask.pocoo.org/docs/api/#flask.Flask.config).

Only *uppercase* values are stored in the config.

There are a few ways to set configuration options. [` dict.update() `](https://docs.python.org/2/library/stdtypes.html#dict.update):

app.config.update(KEYWORD0='value0',  KEYWORD1='value1')
For the future examples, let’s assume this:

- website/  -  __init__.py  -  app.py  -  config/  -  __init__.py  -  dev.py

Inside *website/config/dev.py*:

class  DevConfig(object):  DEBUG  =  True  TESTING  =  True  DATABASE_URL  =  'sqlite://:memory:'

Creating a class and pointing to it via[` flask.Config.from_object() `](http://flask.pocoo.org/docs/api/#flask.Config.from_object) also works:

from  .config.dev  import  DevConfigapp.config.from_object(DevConfig)

Another option with ` from_object() ` is a string of the config object’s location:

app.config.from_object('website.config.dev.DevConfig')

In addition, it’ll work with modules (django’s style of storing settings). For *website/config/dev.py*:

DEBUG  =  TrueTESTING  =  TrueDATABASE_URL  =  'sqlite://:memory:'
Then:
app.config.from_object('website.config.dev')

So, this sounds strange, but as of Flask 1.12, that’s all there is regarding importing classes/modules. The rest is all importing python files.

To import an *object* (module or class) from an environmental variable, do something like:

app.config.from_object(os.environ.get('FLASK_MODULE',  'web.conf.default'))

[` flask.Config.from_envvar() `](http://flask.pocoo.org/docs/api/#flask.Config.from_envvar) is spiritually similar to` DJANGO_SETTINGS_MODULE `, but looks can be deceiving.

The environmental variable set points to a file, which is interpreted like a module.

Tangent: Confusion with configs:

Despite the pythonic use of [` from_object() `](http://flask.pocoo.org/docs/api/#flask.Config.from_object) and the[pattern using classes](http://flask.pocoo.org/docs/config/#config-dev-prod) to store configs for dev/prod setups in official documentation, and the abundance of string to python object importation utilities, environmental variables in Flask don’t point to a class, but to *files* which are interpreted as modules.

There’s a potential [Chesterton’s Fence](https://en.wikipedia.org/wiki/Wikipedia:Chesterton%27s_fence)issue also. I [made an issue](https://github.com/pallets/flask/issues/2368) about it to document my observations. The [maintainer’s response](https://github.com/pallets/flask/issues/2368#issuecomment-308116267)was they’re enhancing the ` FLASK_APP ` environmental variable to [specify an application factory with arbitrary arguments](https://github.com/pallets/flask/blob/b5f4c52/CHANGES#L46).)

In the writer’s opinion, an API-centric framework like flask introducing the ` FLASK_APP ` variable exacerbates the aforementioned confusion. Why add` FLASK_APP ` when [` from_envvar() `](http://flask.pocoo.org/docs/api/#flask.Config.from_envvar) is available? Why not allow [pointing to a config object and leveraging what flask already has and exemplifies in its documentation](https://en.wikipedia.org/wiki/Principle_of_least_astonishment)?

It’s already de facto in the flask community to point to modules and classes when apps bootstrap. There’s a reason for that. Maintainer’s should harken back on using the tools and gears that originally earned flask its respect. In microframeworks, nonorthogonality sticks out like a sore thumb.

Assuming *website/config/dev.py*:
DEBUG  =  TrueTESTING  =  TrueDATABASE_URL  =  'sqlite://:memory:'
Let’s apply a configuration from an environmental variable:
app.config.from_envvars('FLASK_CONFIG')
` FLASK_CONFIG ` should map to a python file:
export  FLASK_CONFIG=website/config/dev.py

Here’s where Flask’s configurations aren’t so orthogonal. There’s also a[` flask.Config.from_pyfile() `](http://flask.pocoo.org/docs/api/#flask.Config.from_pyfile):

app.config.from_pyfile('website/config/dev.py')

### Flask’s Initialization[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#flask-s-initialization)

Flask’s initiation is different then Django’s.

Before any server is started, the [` Flask `](http://flask.pocoo.org/docs/api/#flask.Flask) object must be initialized. The ` Flask ` object acts a registry URL mappings, view callback code (business logic), hooks, and other configuration data.

The ` Flask ` object only requires one argument to initialize, the so-called ` import_name ` parameter. This is used as a way to identify what belongs to your application. For more information on this parameter, see *About the First Parameter* on the [Flask API documentation page](http://flask.pocoo.org/docs/api/#api):

from  flask  import  Flaskapp  =  Flask('myappname')

Above: ` app `, an instantiated ` Flask ` object. No server or configuration present (yet).

#### Dissecting the ` Flask ` object[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#dissecting-the-flask-object)

During the initialization, the ` Flask ` object hollowed out [` dict `](https://docs.python.org/2/library/stdtypes.html#dict)and ` list ` attributes to store “hook” functions, such as:

- [` error_handler_spec `](http://flask.pocoo.org/docs/api/#flask.Flask.error_handler_spec)
- [` url_build_error_handlers `](http://flask.pocoo.org/docs/api/#flask.Flask.url_build_error_handlers)
- [` before_request_funcs `](http://flask.pocoo.org/docs/api/#flask.Flask.before_request_funcs)
- [` before_first_request_funcs `](http://flask.pocoo.org/docs/api/#flask.Flask.before_first_request_funcs)
- [` after_request_funcs `](http://flask.pocoo.org/docs/api/#flask.Flask.after_request_funcs)
- [` teardown_request_funcs `](http://flask.pocoo.org/docs/api/#flask.Flask.teardown_request_funcs)
- [` url_value_preprocessors `](http://flask.pocoo.org/docs/api/#flask.Flask.url_value_preprocessors)
- [` url_default_functions `](http://flask.pocoo.org/docs/api/#flask.Flask.url_default_functions)
- [` template_context_processors `](http://flask.pocoo.org/docs/api/#flask.Flask.template_context_processors)
- [` shell_context_processors `](http://flask.pocoo.org/docs/api/#flask.Flask.shell_context_processors)

See a pattern above? They’re all function callbacks that are triggered upon events occuring. ` template_context_processors ` seems a lot like Django’s [context processor](http://docs.djangoproject.com/en/1.11/ref/templates/api/#subclassing-context-requestcontext)middleware.

- [` blueprints `](http://flask.pocoo.org/docs/api/#flask.Flask.blueprints): blueprints
- [` extensions `](http://flask.pocoo.org/docs/api/#flask.Flask.extensions): extensions
- [` url_map `](http://flask.pocoo.org/docs/api/#flask.Flask.url_map): url mappings
- [` view_functions `](http://flask.pocoo.org/docs/api/#flask.Flask.view_functions): view callbacks

So why list these? Situational awareness is a key matter when using a micro framework. Understanding what happens under the hood ensures confidence the application is handled by the developer, not the other way around.

#### Hooking in views[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#hooking-in-views)

The application object is instantiated relatively early because it’s used to decorate views.

Still, at this point, you don’t have a server running yet. Just a` Flask ` object. Most examples will show the object instantiated as` app `, you can of course use any name.

from  flask  import  Flaskapp  =  Flask(__name__)@app.route('/')def  hello_world():  return  'Hello, World'

The [` flask.Flask.route() `](http://flask.pocoo.org/docs/api/#flask.Flask.route) decorator is just a fancy way of doing[` flask.Flask.add_url_rule() `](http://flask.pocoo.org/docs/api/#flask.Flask.add_url_rule):

from  flask  import  Flaskapp  =  Flask(__name__)def  hello_world():  return  'Hello, World'app.add_url_rule('/',  'hello_world',  hello_world)

#### Configure the Flask object[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#configure-the-flask-object)

See also:

[Configuring Flask](https://www.git-pull.com/code_explorer/django-vs-flask.html#configuring-flask)

Here’s an interesting one: Generally configuration isn’t added until after the *after* initializing the Python object.

You could make a function to act as a factory/bootstrapper for flask objects. There’s nothing magical here, nothing’s tying you down - it’s python. Unlike with django, which controls initialization, a Flask project has to handle minutiae of initialization on its own.

In this situation, let’s wrap it in a pure function:

from  flask  import  Flaskclass  DevConfig(object):  DEBUG  =  True  TESTING  =  True  DATABASE_URL  =  'sqlite://:memory:'def  get_app():  app  =  Flask(__name__)  app.config.from_object(DevConfig)  return  app

#### Start Flask web server[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#start-flask-web-server)

if  __name__  ==  '__main__':  app  =  get_app()  app.run()
See [` flask.Flask.run() `](http://flask.pocoo.org/docs/api/#flask.Flask.run).

*New in version 0.12: *Flask also has a [command-line API](http://flask.pocoo.org/docs/cli/#cli)

### Flask and Databases[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#flask-and-databases)

Unlike Django, Flask doesn’t tie project’s to a database.

There’s no rules saying a Flask app has to connect to a database. It’s python, flask could used to make a proxy/abstraction of a thirdparty REST API. Or a quick web front-end to a pure-python program. Another possiblity, generating a purely static website with no SQL backend [a la NPR](http://blog.apps.npr.org/2014/07/29/everything-our-app-template-does.html).

If a website is using RDBMS, which is often true, a popular choice is SQLAlchemy. [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/) helps assist in gluing them together.

SQLAlchemy is mature (a decade older than this writing), battle-tested with a massive test suite, dialects for many SQL solutions. It also provides something called “[core](http://docs.sqlalchemy.org/en/latest/core/index.html#core-toplevel)” underneath the hood that allows building SQL queries via python objects.

SQLAlchemy is also active. Innovation keeps happening. The change log keeps showing good things happening. Like Django’s ORM, SQLAlchemy’s documentation is top notch. Not to mention, [Alembic](http://alembic.zzzcomputing.com/), a project by the same author, harnesses SQLAlchemy to power migrations.

## Interpretations[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#interpretations)

Software development best practices form over time. Decisions should be made by those with familiarity with their product or service’s needs.

Over the last 10 years, the fundamentals of web projects haven’t shifted. None of Rails’ or Django’s MVC workflows were thrown out the window. On the contrary, they thrived. At the end of the day, the basics still boils down to JSON, HTML templates, CSS, and JS assets.

### Flask is pure, easy to master, but can lend to reinventing the wheel[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#flask-is-pure-easy-to-master-but-can-lend-to-reinventing-the-wheel)

Flask is meant to stay out of the way and put the developer into control. Even over things as granular as piecing together the ` Flask ` object, registering blueprints and starting the web server.

The API is, much like this website, is documented using [sphinx](http://sphinx-doc.org/). The reference will become a goto. To add to it, a smaller codebase means a developer can realistically wrap their brain around the internals.

Developers that find implicit behavior to be a hindrance and thrive in explicitness will feel comfortable using Flask.

However, this comes at the cost of omitting niceties many web projects would actually *find helpful*, not an encumbrance. It’ll also leave developer’s relying on third party extensions. To think of a few that’d come up for many:

What about authentication?

There’s no way to store the users. So grab SQLAlchemy, peewee, or MongoEngine. There’s the database back-end.

Now to building the user schema. Should the website accept email addresses as usernames? What about password hashing? Maybe [Flask-Security](https://flask-security.readthedocs.io/) or[Flask-Login](https://flask-login.readthedocs.io/) will do here.

Meanwhile, [Django would have](https://docs.djangoproject.com/en/1.11/topics/auth/default/) the ORM, User Model, authentication decorators for views, *and*  [` login forms `](http://docs.djangoproject.com/en/1.11/topics/auth/default/#django.contrib.auth.views.LoginView), with database-backed validation. And it’s pluggable and templated.

What about JSON and REST?

If it involves a database backend, that still has to be done (like above). To help Flask projects along, there are solutions like [Flask API](http://www.flaskapi.org/) (inspired by Django Rest Framework) and [Flask-RESTful](https://flask-restful.readthedocs.io/).

#### Flask’s extension community chugs, while Django’s synergy seems unstoppable[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#flask-s-extension-community-chugs-while-django-s-synergy-seems-unstoppable)

That isn’t to say Flask has no extension community. It does. But it lacks the cohesion and comprehensiveness of Django’s. Even in cases where there are extensions, there will be corner cases where features are just missing.

For instance, without an authentical and permissions system, it’s difficult to create an OAuth token system to grant time-block’d permissions to slices of data to make available. Stuff available for free with[django-rest-framework’s django-guardian integration](http://www.django-rest-framework.org/api-guide/permissions/#djangoobjectpermissions), which benefit from both Django’s ORM and its permission system, in many cases aren’t covered by the contrib community at all. This is dicussed in greater detail in [Open source momentum](https://www.git-pull.com/code_explorer/django-vs-flask.html#open-source-momentum).

### Django is comprehensive, solid, active, customizable, and robust[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#django-is-comprehensive-solid-active-customizable-and-robust)

[Batteries included](https://docs.python.org/2/tutorial/stdlib.html#tut-batteries-included).

A deep notion of customizability and using subclassed Field, Forms, Class Based Views, and so on to suit situations.

The components django provided complement each other.
Rather than dragging in hard-requirements, nothing forces you to:

- use the Form framework
- if using the Form framework, to:
    - back forms with models (ModelForm)
    - output the form via [` as_p() `](http://docs.djangoproject.com/en/1.11/ref/forms/api/#django.forms.Form.as_p),[` as_table() `](http://docs.djangoproject.com/en/1.11/ref/forms/api/#django.forms.Form.as_table), or[` as_ul() `](http://docs.djangoproject.com/en/1.11/ref/forms/api/#django.forms.Form.as_ul)
- use class-based views
- use a *specific* class-based view
- if using a class-based view, fully implement every method of a specialized-view
- use django’s builtin User model

Above are just a few examples, but Django doesn’t strap projects into using every battery.

That said, the [` QuerySet `](http://docs.djangoproject.com/en/1.11/ref/models/querysets/#django.db.models.query.QuerySet) object plays a huge role in catalyzing the momentum django provides. It provides easy database-backed form validations, simple object retrieval with views, and code readability. It’s even utilized downstream by extensions like django-filters and django-tables2. These two plugins don’t even know about each other, but since they both operate using the same database object, you can use django-filter’s filter options to facet and search results that are produced by django-tables2.

### Open source momentum[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#open-source-momentum)

Flask, as a microframework, is relatively dormant from a feature standpoint. Its scope is well-defined.

Flask isn’t getting bloated. Recent pull requests seem to be on tweaking and refining facilities that are already present.

It’s not about stars, or commits, or contributor count. It’s about features and support niceties that can be articulated in [change logs](https://github.com/pallets/flask/blob/master/CHANGES).

Even then though, it’s hard to put things into proportion. Flask includes[Werkzeug](http://werkzeug.pocoo.org/) and [Jinja2](http://jinja.pocoo.org/) as hard dependencies. They run as independent projects (*i.e. their own issue trackers*), under the [pallets organization](https://github.com/pallets).

Django wants to handle everything on the web backend. Everything fits together. And it needs to, because it’s a framework. Or a framework of frameworks. Since it covers so much ground, let’s try once again to put it into proportion, against Flask:

| Django | Flask |
| --- | --- |
| Django ORM | SQLAlchemy, MongoEngine |
| Django Migrations | Alembic |
| Django Templates | Jinja2 |
| Django Core / URL’s | Werkzeug |
| Django Forms (ModelForm) | WTForms ([WTForms-Alchemy](https://wtforms-alchemy.readthedocs.io/)) |
| Django Commands | Flask-Script (flask bundles [CLI support](http://flask.pocoo.org/docs/cli/#cli) as of 0.11) |

There are also feature requests that come in, often driven by need of the web development community, and things that otherwise wouldn’t be considered for Flask or Flask extension. Which kind of hurts open source, because there’s code that could be reuseable being written, but not worth the effort to make an extension for. So there are [snippets](http://flask.pocoo.org/snippets/) for that.

And in a language like Python where packages, modules, and duck typing rule, I feel snippets, while laudable, are doomed to fall short keeping in check perpetual recreation of patterns someone else done. Not to mention, snippets don’t have CI, nor versioning, nor issue trackers (maybe a comment thread).

By not having a united front, the oppurtunity for synergetic efforts that bridge across extensions (a la Django ORM, Alchemy, DRF, and django-guardian) fail to materialize, creating extensions that are porous. This leaves devs to fill in the blanks for all-inclusive functionality that’d already be working had they just picked a different tool for the job.

## Conclusion[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#conclusion)

We’ve covered Flask and Django, their philosophies, their API’s, and juxtaposed those against the writer’s personal experiences in production and open source. The article included links to specific API’s across a few python libraries, documentation sections, and project homepages. Together, they should prove fruitful in this being a resource to come back to.

Flask is great for a quick web app, particularly for a python script to build a web front-end for.

If already using SQLAlchemy models, it’s possible to get them working with a Flask application with little work. With Flask, things feel in control.

However, once relational databases come into play, Flask enters a cycle of diminishing returns. Before long, projects will be dealing with forms, REST endpoints and other things that are all best represented via a declarative model with types. The exact stance [Django’s applications](http://docs.djangoproject.com/en/1.11/ref/applications/)take from the beginning.

There’s an informal perception that [Batteries included](https://docs.python.org/2/tutorial/stdlib.html#tut-batteries-included)may mean a growing list of ill-maintained API’s that get hooked into every request. In the case of Django, everything works across the board. When an internal Django API changes, Django’s testsuites to break and the appropriate changes are made. So stuff integrates. This is something that’s harder to do when there’s a lot of packages from different authors who have to wait for fixes to be released in Flask’s ecosystem.

And if things change. I look forward to it. Despite Flask missing out on Django’s synergy, it is still a mighty, mighty microframework.

### Bonus: Cookiecutter template for Flask projects[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#bonus-cookiecutter-template-for-flask-projects)

Since I still use Flask. I maintain a [cookiecutter](https://cookiecutter.readthedocs.io/)[template project for it](https://github.com/tony/cookiecutter-flask-pythonic).

This cookiecutter project will create a core application object that can load Flask blueprints via a declarative YAML or JSON configuration.

Feel free to use it as a sample project. In terminal:
pip install --user cookiecutter

cookiecutter https://github.com/tony/cookiecutter-flask-pythonic.gitcd ./path-to-project

virtualenv .env && . .env/bin/activate
pip install -r requirements.txt
./manage.py

### Bonus: How do I learn Django or Flask?[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#bonus-how-do-i-learn-django-or-flask)

#### Preparation[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#preparation)

- Understand how python [virtual environments](https://python-guide.readthedocs.io/en/latest/dev/virtualenvs/) and [PATH](https://en.wikipedia.org/wiki/PATH_(variable))’s work:
    - [Real Python’s tutorial on virtualenvs](https://realpython.com/blog/python/python-virtual-environments-a-primer/).
    - Check out my book *The Tao of tmux*  [available online free](https://leanpub.com/the-tao-of-tmux/read) for some good coverage of the terminal.
- For learning python, here are some free books:
    - [Learn Python the Hard Way](https://learnpythonthehardway.org/book/)
    - [The Hitchhiker’s Guide to Python](https://python-guide.readthedocs.io/)
- Grab [Django’s documentation PDF](https://media.readthedocs.org/pdf/django/latest/django.pdf) and [Flask’s documentation PDF](http://flask.pocoo.org/docs/dev/.latex/Flask.pdf). Read it on a smart phone or keep it open in a PDF reader.
- Get in the habit of reading python docs on [ReadTheDocs.org](https://www.readthedocs.org/), a documentation hosting website.

#### Developing[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#developing)

- Make a hobby website in django or flask.

Services like [Heroku](https://www.heroku.com/) are free to try, and simple to deploy Django websites to.

For more free hosting options see https://github.com/ripienaar/free-for-dev.

DigitalOcean plans [start at $5/mo](https://m.do.co/c/a8d3c8586c91)per instance. Supports FreeBSD with ZFS.

- Bookmark and study to this article to get the latest on differences between Django and Flask. While it’s a comparison, it’ll be helpful in curating the API and extension universe they have.
- For free editors, check out good old [vim](http://www.vim.org/) + [python-mode](https://github.com/python-mode/python-mode), [Visual Studio Code](https://code.visualstudio.com/), [Atom](https://atom.io/), or [PyCharm](https://www.jetbrains.com/pycharm/)

## Future articles[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#future-articles)

I’m considering creating some articles or books that go deeper into Python internals.

- Django’s ORM
- Django’s startup
- Flask’s internals / code overview
- Django’s internals / code overview
- Numpy, Pandas internals
- CPython internals
- Pypy internals

Talking through the code and patterns in large-scale applications is a good way to teach others. In lieu of that, they’re fun to read. If you have a request, send an email, tony @ git-pull.com

## Hire me[¶](https://www.git-pull.com/code_explorer/django-vs-flask.html#hire-me)

Looking to hire a Flask or Django developer remote? Teacher? Send me an email, tony at git-pull.com.

Like my stuff? [Your support is appreciated!](https://www.git-pull.com/support.html#support)