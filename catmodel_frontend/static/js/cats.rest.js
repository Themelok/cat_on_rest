myApp.factory('Cats', function($resource) {
  return $resource('/api/cats/:id', {'id': '@id'});
});