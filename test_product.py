from products import Product
import pytest

# @pytest.mark.test_product
# @pytest.mark.test_creating_product
# @pytest.mark.test_creating_product_invalid_details
# @pytest.mark.test_prod_becomes_inactive
# @pytest.mark.buy_modifies_quantity
# @pytest.mark.buy_too_much

@pytest.mark.test_product
@pytest.mark.test_prod_becomes_inactive
def test_creating_product():
    prod = Product("MacBook Air M2", price=1450, quantity=100)
    assert isinstance(prod, Product) # use assert for positive test cases with pytest

@pytest.mark.test_product
@pytest.mark.test_creating_product_invalid_details
@pytest.mark.parametrize(
    "invalid_size, expected_exception",
    [
        (1, ValueError), # checking for non-string name
        ("", ValueError) # checking for empty string name
    ]
)
def test_creating_product_name(invalid_size, expected_exception):
    # Name
    with pytest.raises(expected_exception): # use pytest.raises() for negative test cases with pytest
        Product(invalid_size, price=1450, quantity=100)

@pytest.mark.test_product
@pytest.mark.test_creating_product_invalid_details
@pytest.mark.parametrize(
    "invalid_size, expected_exception",
    [
        (-1.0, ValueError), # checking for negative price
        ("20", ValueError) # checking for non-numeric price
    ]
)
def test_creating_product_price(invalid_size, expected_exception):
    # Price
    with pytest.raises(expected_exception):
        Product("MacBook Air M2", price=invalid_size, quantity=100)

@pytest.mark.test_product
@pytest.mark.test_creating_product_invalid_details
@pytest.mark.parametrize(
    "invalid_size, expected_exception",
    [
        (-1, ValueError), # checking for negative quantity
        (20.3, ValueError), # checking for non-int quantity
        ("20", ValueError) # checking for non-int quantity
    ]
)
def test_creating_product_quantity(invalid_size, expected_exception):
    # Price
    with pytest.raises(expected_exception):
        Product("MacBook Air M2", price=100, quantity=invalid_size)

@pytest.mark.test_product
@pytest.mark.test_prod_becomes_inactive
def test_prod_becomes_inactive():
    prod = Product("MacBook Air M2", price=1450, quantity=100)
    prod.set_quantity(0)
    assert prod.is_active() == False

@pytest.mark.test_product
@pytest.mark.buy_modifies_quantity
def test_buy_modifies_quantity():
    prod = Product("MacBook Air M2", price=1450, quantity=100)
    prod.buy(50)
    assert prod.get_quantity() == 50

@pytest.mark.test_product
@pytest.mark.buy_too_much
def test_buy_too_much():
    prod = Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(ValueError):
        prod.buy(150)