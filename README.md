Commands Django Shell
1. Создание User
   1. user1 = User.objects.create_user(username='Dim', first_name='Dima')
   2. user2 = User.objects.create_user(username='IG', first_name='Igor')
2. Создание двух объектов класса Author
   1. Author.objects.create(authorUser=user1)
   2. Author.objects.create(authorUser=user2)
3. Добавление 4-х категорий
   1. Category.objects.create(name='IT')
   2. Category.objects.create(name='Edu')
   3. Category.objects.create(name='Book')
   4. Category.objects.create(name='Info')
4. Добавление двух статей и одной новости и присвоение им категорий
   1. Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Dim')), category = 'NW', title='WNews', text='text')
   2. Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='IG')), category = 'NW', title='WNews2', text='textTEXTtext')
   3. Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='IG')), category = 'AR', title='title23232', text='2222textTEXTtext')
5. Комментирование текста
   1. Comment.objects.create(commentUser=User.objects.get(username='Dim'), commentPost=Post.objects.get(pk=1), text='comment text1')
   2. Comment.objects.create(commentUser=User.objects.get(username='Dim'), commentPost=Post.objects.get(pk=3), text='comment text3')
   3. Comment.objects.create(commentUser=User.objects.get(username='Dim'), commentPost=Post.objects.get(pk=2), text='comment text2')
6. Методы like() и dislike()
   1. Post.objects.get(pk=1).like()
   2. Post.objects.get(pk=1).like()
   3. Post.objects.get(pk=1).like()
   4. Post.objects.get(pk=2).like()
   5. Post.objects.get(pk=3).dislike()
7. Обновление рейтинга пользователей
   1. Author.objects.get(authorUser=User.objects.get(username='Dim')).update_rating()
   2. Author.objects.get(authorUser=User.objects.get(username='IG')).update_rating()
8. Вывод username и рейтинг автора
   1. a = Author.objects.get(authorUser=User.objects.get(username='Dim'))
      1. a.ratingAuthor
9. Вывод лучшего пользователя
   1. best = Author.objects.all().order_by('-ratingAuthor').values('authorUser', 'ratingAuthor')[0]
   2. print(best)
10. Вывод всех комментариев
    1.  comm = Comment.objects.all().values('rating', 'dateCreation')
