# HashTag

* HashTag 모델 설정
* Article에 hashtag M:N관계로 설정
  * `hashtag = models.ManyToManyField(HashTag, )

* 게시글의 content내에 들어온 데이터 내에서 #를 달고 있는 단어들을 뽑아내야함

  ```python
  for word in article.cotent.split():
      if word.startswith('#'):
  		hashtag, boolean = HashTag.objects.get_or_create(content=word)
          # 생성 했으면 True, 이미 존재해서 생성 안하면 False
          article.hashtags.add(hashtag)
  ```

  

* 