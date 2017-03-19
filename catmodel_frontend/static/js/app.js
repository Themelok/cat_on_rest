var myApp = angular.module('catmodelFrontendApp', ['ngResource']);


//Trailing slashes
myApp.config(function($resourceProvider) {
  $resourceProvider.defaults.stripTrailingSlashes = false;
});

myApp.controller('MainCtrl', function($scope, Cats, Authors)
{
    console.log('In main Control');
    $scope.cats = Cats.query();
    $scope.auth = Authors.query();

    $scope.newCats = {};
    $scope.newAuthor={};

    $scope.uploadAuthor = function()
    {
        // call REST API endpoint
        Authors.save($scope.newAuthor).$promise.then(
            function(response) {
                // the response is a valid image, put it at the front of the images array
                $scope.auth.unshift(response);
            },
            function(rejection) {
                console.log('Failed to upload author');
                console.log(rejection);
            }
        );
    };


    $scope.uploadCats = function()
    {
        // call REST API endpoint
        Cats.save($scope.newCats).$promise.then(
            function(response) {
                // the response is a valid image, put it at the front of the images array
                $scope.cats.unshift(response);
            },
            function(rejection) {
                console.log('Failed to upload cat');
                console.log(rejection);
            }
        );
    };
});