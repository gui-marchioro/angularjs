app.controller('OrdersController', function ($scope, $routeParams, customersService) {
    var customerId = $routeParams.customerId;
    $scope.customer = null;

    function init() {
        customersService.getCustomer(customerId)
            .then(function(customer) {
                $scope.customer = customer.data;
            })
            .catch(function(data, status, headers, config) {
                // handle error
            });
    }

    init();
});
