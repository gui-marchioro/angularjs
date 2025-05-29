app.factory('customersFactory', function ($http) {
    var factory = {};
    factory.getCustomers = function() {
        return $http.get('/customers');
    };
    factory.getCustomer = function(customerId) {
        return $http.get('/customers/' + customerId);
    }

    return factory;
});