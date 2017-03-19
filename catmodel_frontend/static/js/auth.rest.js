myApp.factory('Authors', function($resource) {
  return $resource('/api/authors/:id', {'id': '@id'},{
        'save':{
        method: 'POST',
        transformRequest: transAuthorRequest,
        headers:{'Content-Type':undefined}
        },
    });
});


// CopyPaste from http://stackoverflow.com/a/21115779
function transAuthorRequest(data) {
    if (data === undefined)
        return data;

    var fd = new FormData();
    angular.forEach(data, function(value, key) {
      if (value instanceof FileList) {
        if (value.length == 1) {
          fd.append(key, value[0]);
        } else {
          angular.forEach(value, function(file, index) {
            fd.append(key + '_' + index, file);
          });
        }
      } else {
        fd.append(key, value);
      }
    });

    return fd;
}