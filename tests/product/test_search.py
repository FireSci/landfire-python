"""ProductSearch tests."""
import pytest

from landfire.product.enums import ProductRegion, ProductTheme, ProductVersion
from landfire.product.search import ProductSearch


PRODUCT_LIST_LEN = 76


@pytest.fixture
def search() -> ProductSearch:
    """A ProductSearch fixture."""
    return ProductSearch()


def test_init_product_search() -> None:
    """Test ProductSearch() instantiates and has product list of length==76."""
    search = ProductSearch()
    assert isinstance(search, ProductSearch)


def test_search_products_no_params(search: ProductSearch) -> None:
    """Test ProductSearch.get_products() uses no filters."""
    products = search.get_products()
    assert len(products) == PRODUCT_LIST_LEN


def test_search_products_names(search: ProductSearch) -> None:
    """Test ProductSearch.get_products() filters by name."""
    products = search.get_products(
        names=["fuel vegetation cover 2020", "landfire map zones"]
    )
    assert len(products) == 2


def test_search_products_codes(search: ProductSearch) -> None:
    """Test ProductSearch.get_products() filters by code."""
    products = search.get_products(codes=["FBFM40"])
    assert len(products) == 4


def test_search_products_themes(search: ProductSearch) -> None:
    """Test ProductSearch.get_products() filters by theme."""
    products = search.get_products(themes=[ProductTheme.disturbance, ProductTheme.fuel])
    assert len(products) == 44


def test_search_products_versions(search: ProductSearch) -> None:
    """Test ProductSearch.get_products() filters by version."""
    products = search.get_products(versions=[ProductVersion.lf_2001])
    assert len(products) == 23


def test_search_products_regions(search: ProductSearch) -> None:
    """Test ProductSearch.get_products() filters by region."""
    products = search.get_products(regions=[ProductRegion.HI])
    assert len(products) == 54


def test_search_products_regions_two(search: ProductSearch) -> None:
    """Test ProductSearch.get_products() filters by regions."""
    products = search.get_products(regions=[ProductRegion.HI, ProductRegion.AK])
    assert len(products) == 57


def test_search_products_regions_three(search: ProductSearch) -> None:
    """Test ProductSearch.get_products() filters by regions."""
    products = search.get_products(
        regions=[ProductRegion.HI, ProductRegion.AK, ProductRegion.US]
    )
    assert len(products) == PRODUCT_LIST_LEN


def test_search_products_combination(search: ProductSearch) -> None:
    """Test ProductSearch.get_products() filters by several args."""
    products = search.get_products(
        versions=[ProductVersion.lf_2001],
        themes=[ProductTheme.fire_regime],
        codes=["MFRI"],
        names=["mean fire return interval"],
    )
    assert len(products) == 1


def test_search_products_get_layers(search: ProductSearch) -> None:
    """Test ProductSearch.get_layers() returns filtered layers."""
    layers = search.get_layers(names=["disturbance"])
    assert len(layers) == 22
