def update_loading(loading, unit):
  loading_progress = loading
  loading_progress += unit
  if loading_progress > 100:
    loading_progress = 100
  return loading_progress