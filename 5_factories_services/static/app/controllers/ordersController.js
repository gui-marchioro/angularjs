app.controller('OrdersController', function ($scope, $routeParams, $log, customersService) {
    var customerId = $routeParams.customerId;
    $scope.customer = null;

    function init() {
        customersService.getCustomer(customerId)
            .then(function(customer) {
                $scope.customer = customer.data;
            })
            .catch(function(data, status, headers, config) {
                $log.log('Status: ' + status + ', ' + data.error);
            });
    }

    init();
});
