class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        filtered = []
        for product in self.products:
            if product[0] == first_letter:
                filtered.append(product)

        return filtered

    def __repr__(self):
        result = f"Items in the {self.name} catalogue:"

        for product in sorted(self.products):
            result += "\n" + product

        return result