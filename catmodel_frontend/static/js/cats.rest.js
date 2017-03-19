//myApp.factory('Cats', function($resource) {
//  return $resource('/api/cats/:id', {'id': '@id'});
//});
myApp.factory('Cats', function($resource) {
  return $resource('/api/cats/:id', {'id': '@id'},{
        'save':{
        method: 'POST',
        transformRequest: transRequest,
        headers:{'Content-Type':undefined}
        },
    });
});
