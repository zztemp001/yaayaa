# Overview

This package creates a minimal framework for creating AJAX endpoints of your own in Django without having to create all of the mappings, handling errors, building JSON, etc.

Additionally, this package allows you to create AJAX endpoints for manipulating Django models directly from JavaScript without much effort. This feature works in a similar manner to Django's `ModelAdmin` feature in `admin.py`.

# Install

1. Make sure you have the [decorator](http://pypi.python.org/pypi/decorator) package installed.
2. Install the `ajax/` directory as you would any other application in your Django project or put it in your Django project's `sys.path` somewhere. 
3. Add `ajax` to `INSTALLED_APPS` in your `settings.py`.
4. In your Django project's `urls.py` add `(r'^ajax/', include('ajax.urls'))`.

There are no models associated with this package so you don't need to worry about syncing your database or anything.

# Usage

You can use this package to create ad-hoc AJAX endpoints or by exposing your Django applications's models via AJAX.

1. `/ajax/{some_app_name}/{some_endpoint}.json` is treated as an ad-hoc AJAX endpoint and will be mapped to `some_app_name.endpoints.some_endpoint`. The function `some_endpoint` must return a `dict` or an `HttpResponse` of some sort. When a `dict` is returned, it is serialized as JSON and packaged up nicely for the client.
2. `/ajax/{some_app_name}/{model}.json` will attempt to load up an instance of `ModelEndpoint` for the given model and run an append operation to create a new record for the given model.
3. `/ajax/{some_app_name}/{model}/{pk}/(update|delete|get).json` will attempt to load up an instance of `ModelEndpoint` for the given model and run the given operation for the record specified by `pk`.

All of your AJAX endpoints should be put into a file called `endpoints.py` in your Django applications. AJAX will handle all of the rest of the magic.

## Ad-Hoc Endpoint

The following is a simple example of an AJAX endpoint that just echo's back the POST. Keep in mind that ad-hoc AJAX endpoints basically work like regular Django views in that they get a `request` object. All of the usual view decorators can be used here without issue (e.g. `login_required`). The only thing to keep in mind is that views *only* get `request` as an argument and *must* return a `dict` or `HttpResponse`.

    from ajax.exceptions import AJAXError

    def right_back_at_you(request):
        if len(request.POST):
            return request.POST
        else:
            raise AJAXError(500, 'Nothing to echo back.')

If you're surfacing a known error, it's best to use `AJAXError` with a sane error code and a message. All other exceptions will be returned as a 500 with a generic error message. 

From JavaScript you can easily access the endpoint using jQuery.

    $.post('/ajax/my_app/right_back_at_you.json', {
        name: "Joe Stump",
        age: 31
    });

You can also create endpoints from callable objects. The `BaseEndpoint` class has two functions that are pretty helpful for encoding Django a `QuerySet` or an instance of `Model`.

	# BaseEndpoint._encode_*` appears to have been depricated. 
	# You should use ajax.encoders.encoder in the future:

	from ajax.encoders import encoder
	encoder.encode(record)


* `BaseEndpoint._encode_data` takes a single argument, `data`, which it assumes to be a `QuerySet` (or something that looks and acts like one) and converts it into a vanilla list capable of being serialized using `simplejson`. This uses Django's Python serializer and does some minor cleanup to make it a sane looking JSON payload.
* `BaseEndpoint._encode_record` takes a Django `Model` and encodes it into a normal Python dict. Additionally, it looks for `ForeignKey`'s and hydrates them to include the full associated record.

The following code is a simple example of using the `BaseEndpoint._encode_record` method. You could easily encode a bunch of users with `BaseEndpoint._encode_data` by replacing a few lines of code in this example.

    from django.contrib.auth.models import User
    from ajax.endpoints import BaseEndpoint
    from ajax.exceptions import AJAXError

    class MyEndpoint(BaseEndpoint):
        __call__(self, request):
            try:
                user = User.objects.get(pk=int(request.POST['user']))
            except User.DoesNotExist:
                raise AJAXError(404, 'Invalid user.')

            return self._encode_record(user)

    my_endpoint = MyEndpoint()

## Model Endpoint

AJAX also offers a class, called `ModelEndpoint`, that takes a Django model and exposes ways to manipulate it via AJAX.

    import ajax
    from my_app.models import Category
    
    class CategoryEndpoint(ajax.endpoints.ModelEndpoint):
        pass

    ajax.endpoint.register(Category, CategoryEndpoint)

You can then send a POST to:

* `/ajax/my_app/category.json` to create a new `Category`.
* `/ajax/my_app/category/{pk}/update.json` to update a `Category`. `pk` must be present in the path for `update`, `delete`, and `get`. **NOTE:** This package assumes that the `pk` argument is an integer of some sort. If you've mangled your `pk` fields in weird ways, this likely will not work as expected.
* `/ajax/my_app/category/{pk}/get.json` to get the `Category` as specified as `pk`.
* `/ajax/my_app/category/{pk}/delete.json` to delete the `Category` as specified by `pk`.

**NOTE:** Your Model name (e.g. `category` in the above example) *must* be lowercase. Your request will fail otherwise.

### Adding Ad-hoc endpoints to ModelEndpoints

You can also add you own custom methods to a ModelEndpoint. Adhoc methods in a ModelEndpoint observe the same rules as the get(), update() and delete() methods - with the noticable exception that self.pk _may_ not be set.

For example, you could add a method called `about` that will display some info about the Model or Record (just used for illustration: not actually a good idea in real life):

	import ajax
    from my_app.models import Category
    
    class CategoryEndpoint(ajax.endpoints.ModelEndpoint):	
		
		...
		
		def about(self,request):
			pk = self.pk
        	if pk:
           		return {"message" : "run an operation on record: %s"%self._get_record()}        
        	else:
           		return {"message" : "run an operation on model: %s"%self.model.__name__}
			
Now, in addition to the endpoints above, this method would be available at:

* `/ajax/my_app/category/about.json` - would return "run an operation on model: ..."

or

* `/ajax/my_app/category/{pk}/about.json` - would return "run an operation on record: ..."


### ForeignKey while Fetching

It should be noted that the AJAX package takes a liberal approach when it comes to instances of `ForeignKey` it finds in model declarations. If a model that has a `ForeignKey` is fetched it will be expanded to the full record, recursively. For instance, if a `ForeignKey` to `User` is in a given model, you will get the *whole* associated `User` record when a row is fetched.

### ForeignKey while Creating

In addition to expanding `ForeignKey` while fetching, they are expanded when creating a record from the data in POST. If a `ForeignKey` to `User` is in a given model, and the field is called `author`, `ModelEndpoint` will detect that and automatically assume that `request.POST['author']` is an appropriate `pk`, instantiate it, and replace it with a full instance of the associated `User` object.

### Support for django-taggit

The popular [django-taggit](https://github.com/alex/django-taggit/) is great for adding tags to your Django models. The entire `django-taggit` [API](http://django-taggit.readthedocs.org/en/latest/api.html) is exposed via AJAX for models that have the `tags` attribute. 

* `/ajax/my_app/mymodel/{pk}/tags/add.json` will add the tags specified by the `POST` parameter `tags`, which is a comma separated list of tags.
* `/ajax/my_app/mymodel/{pk}/tags/remove.json` will remove the tags specified by the `POST` parameter `tags`.
* `/ajax/my_app/mymodel/{pk}/tags/set.json` will replace the object's tags specified by `pk` with the tags specified by the `POST` parameter `tags`.
* `/ajax/my_app/mymodel/{pk}/tags/clear.json` will clear all tags from the `pk` specified.
* `/ajax/my_app/mymodel/{pk}/tags/similar.json` will fetch objects that are similarly tagged to the `pk` specified.

**NOTE:** The filtering options in the `django-taggit` API are not available via AJAX at this point.





# Security

There are a number of security features inherent in the framework along with ways to lock down your ad-hoc and model endpoints. You can use the decorator(s) outlined below as well as throwing appropriate `AJAXError` exceptions from your ad-hoc endpoints. Of course, all exceptions raised and `HttpResponse` objects returned are respected by default. For model endpoints you can, additionally, use `can_create()`, `can_update()`, `can_delete()`, `can_get()`, and `authenticate()` to lock down various operations on the given model.

## Framework Security

* All requests to an AJAX endpoint must be sent via `POST`, including a GET on a model's `pk`. 
* The default `ModelEndpoint.authenticate()` method requires that a user is, at a minimum, logged in.

## Decorators

The AJAX package offers a familiar decorator in `ajax.decorators` called `login_required`. It works in the same way that the Django decorator does and handles throwing a proper `AJAXError` if the user isn't logged in.

    from ajax.decorators import login_required

    @login_required
    def my_ajax_endpoint(request):
        return {
            'Hello, %s!' % request.user.username
        }

## ModelEndpoint

The `ModelEndpoint` class offers a number of methods that you can override to add more advanced security over your model-based enpoints. You can override these in your model-based endpoints to control who is able to access each model and in what manner.

### (bool) ModelEndpoint.can_create(user)

Returns `True` if the `user` can create a new `record` using the given model.

### (bool) ModelEndpoint.can_update(user, record)

Returns `True` if the `user` can update the given `record`.

### (bool) ModelEndpoint.can_delete(user, record)

Returns `True` if the `user` can delete the given `record`.

### (bool) ModelEndpoint.can_get(user, record)

Returns `True` if the `user` can fetch the given `record`.

### (bool) ModelEndpoint.authenticate(request, application, method)

This method is ran before any other security-related operations. This method allows you to control overall authentication-related access prior to any of the `can_*` methods being ran and before any model operations are executed. It is ran regardless of the operation being attempted.

# Todo

1. Integrate [Django's CSRF token support](http://docs.djangoproject.com/en/dev/ref/contrib/csrf/). 
