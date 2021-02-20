template = """
<form action="post">
  {% csrf_token %}
  <input type="hidden" name="drink_id" value="{{drink.id}}">
  <button type="submit">Order it!</button>
</form>
"""