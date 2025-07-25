app.controller('CustomersController', function ($scope, $log, customersService, appSettings) {
    $scope.sortBy = 'name';
    $scope.reverse = false;
    $scope.customers = [];
    $scope.appSettings = appSettings;

    function init() {
        customersService.getCustomers()
            .then(function(customers) {
                $scope.customers = customers.data;
            })
            .catch(function(data, status, headers, config) {
                $log.log('Status: ' + status + ', ' + data.error);
            });
    };

    init();

    $scope.doSort = function(propName) {
        $scope.sortBy = propName;
        $scope.reverse = ! $scope.reverse;
    }
});
