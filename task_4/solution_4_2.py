for i in range(10):
  form = ''
  lemma = ''
  id = ''
  user_input = input()
  if user_input == '' : 
    pass
  elif user_input[0] == '#' :
    pass
  else :
    for letter in user_input :
      id = id + letter
      if letter == '\t' :
        break
    id_length = len(id)
    user_input = user_input[id_length:]
    for letter in user_input :
      form = form + letter
      if letter == '\t' :
        break
    form_length = len(form)
    user_input = user_input[form_length:]
    for letter in user_input :
      lemma = lemma + letter
      if letter == '\t' :
        break
    lemma_length = len(lemma) - 1
    new_form = form[:lemma_length] + '\t'
    if (form != lemma and lemma != new_form) :
      print(form, lemma)
