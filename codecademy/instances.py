class Store:
  def store_name(self, name):
    return name

alternative_rocks = Store()
alt_rocks_store_name = alternative_rocks.store_name = 'Alternative Rocks'
print(alt_rocks_store_name)

isabelles_ices = Store()
isa_ices_store_name = isabelles_ices.store_name = 'Isabelle\'s Ices'
print(isa_ices_store_name)