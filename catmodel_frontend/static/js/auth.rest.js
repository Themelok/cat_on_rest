myApp.factory('Authors', function($resource) {
  return $resource('/api/authors/:id', {'id': '@id'},{
        'save':{
        method: 'POST',
        transformRequest: transRequest,
        headers:{'Content-Type':undefined}
        },
    });
});
