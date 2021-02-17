PAGE_LIMIT = 10

def paginate(page, selection):
  start = (int(page) - 1) * PAGE_LIMIT
  end = start + PAGE_LIMIT
  formated_data = [obj.format() for obj in selection[start:end]]
  return formated_data
