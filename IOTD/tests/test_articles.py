# import os

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "IOTD.settings")

# from django.core.wsgi import get_wsgi_application

# application = get_wsgi_application()

# from users.models import User
# from articles.models import Article, Comment
# from rest_framework.test import APITestCase
# from django.urls import reverse
# from rest_framework import status
# import pytest


# @pytest.mark.django_db
# class ArticlesViewTest(APITestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.user_data = {"email": "test@test.com", "password": "test"}
#         cls.articles_data = {"title": "title", "content": "content", "tags": "tags"}
#         cls.user = User.objects.create_user("test@test.com", "test")

#     def setUp(self):
#         self.access_token = self.client.post(
#             reverse("token_obtain_pair"), self.user_data
#         ).data["access"]
#         # response = self.client.get(
#         #     path=reverse("user_view"), HTTP_AUTHORIZATION=f"Bearer {access_token}"
#         # )
#         # self.assertEqual(response.status_code, 200)

#     # 테스트 후 이미지 파일 삭제하기
#     # def tearDown(self):
#     #     for articles in Article.objects.all():
#     #         articles.delete()

#     # 게시글 작성
#     def test_create_articles_success(self):
#         response = self.client.post(
#             path=reverse("article_view"),
#             data=self.articles_data,
#             HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
#         )
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Article.objects.count(), 1)

#     # 게시글 모두보기(아무것도 없을 때)
#     # def test_get_articles_list_empty(self):
#     #     response = self.client.get(path=reverse("article_view"))
#     #     print(response.json())
#     #     self.assertEqual(response.status_code, status.HTTP_200_OK)
#     #     self.assertEqual(len(response.data), 0)

#     # 게시글 모두보기(게시글 5개)
#     def test_articles_list(self):
#         self.articles = []
#         for _ in range(5):
#             self.articles.append(
#                 Article.objects.create(**self.articles_data, user=self.user)
#             )
#         response = self.client.get(
#             path=reverse("article_view"),
#             HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 5)


# # view = PostingDetailView, url name = "posting_view", method = get, put, delete


# @pytest.mark.django_db
# class PostingDetailViewTest(APITestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.user_data = {"email": "test@test.com", "password": "test"}
#         cls.articles_data = [
#             {"title": "test", "content": "test content1"},
#             {"title": "test2", "content": "test content2"},
#             {"title": "test3", "content": "test content3"},
#             {"title": "test4", "content": "test content4"},
#             {"title": "test5", "content": "test content5"},
#         ]
#         cls.user = User.objects.create_user("test@test.com", "test")
#         cls.articles = []
#         for i in range(5):
#             cls.articles.append(
#                 Article.objects.create(**cls.articles_data[i], user=cls.user)
#             )

#     def setUp(self):
#         self.access_token = self.client.post(
#             reverse("token_obtain_pair"), self.user_data
#         ).data["access"]

#     # 게시글 상세보기
#     def test_articles_detail(self):
#         response = self.client.get(
#             path=reverse("article_detail_view", kwargs={"article_id": 5}),
#             HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data["content"], "test content5")

#     # # 게시글 수정하기
#     def test_articles_detail_update(self):
#         response = self.client.put(
#             path=reverse("article_detail_view", kwargs={"article_id": 5}),
#             data={"title": "updated test Title", "content": "updated test content"},
#             HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(Article.objects.count(), 5)
#         self.assertEqual(response.data["content"], "updated test content")

#     # # 게시글 삭제하기
#     def test_articles_detail_delete(self):
#         response = self.client.delete(
#             path=reverse("article_detail_view", kwargs={"article_id": 5}),
#             HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
#         )
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Article.objects.count(), 4)


# # view = CommentView, url name = "comment_view", method = get, post
# class CommentViewTest(APITestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.user_data = {"email": "test@test.com", "password": "test"}
#         cls.article_data = {"title": "test", "content": "test content"}
#         cls.comment_data = {"content": "test content"}
#         cls.user = User.objects.create_user("test@test.com", "test")
#         cls.articles = Article.objects.create(**cls.article_data, user=cls.user)

#     def setUp(self):
#         self.access_token = self.client.post(
#             reverse("token_obtain_pair"), self.user_data
#         ).data["access"]

#     # 코멘트 작성
#     # def test_create_articles_success(self):
#     #     response = self.client.post(
#     #         path=reverse("comment_view"),
#     #         data=self.comment_data,
#     #         HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
#     #     )
#     #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#     #     self.assertEqual(Comment.objects.count(), 1)
#     #     self.assertEqual(Comment.objects.get().content, "test content")

#     # 코멘트 리스트 모두보기(아무것도 없을 때)
#     # def test_comment_list_empty(self):
#     #     response = self.client.get(
#     #         path=reverse("comment_view", kwargs={"article_id": 1}),
#     #         HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
#     #     )
#     #     self.assertEqual(response.status_code, status.HTTP_200_OK)
#     #     self.assertEqual(response.data, [])

#     # # 코멘트 리스트 모두보기(5개)
#     # def test_comment_list(self):
#     #     self.comments = []
#     #     for _ in range(5):
#     #         self.comments.append(
#     #             Comment.objects.create(
#     #                 **self.comment_data, posting=self.articles, user=self.user
#     #             )
#     #         )
#     #     response = self.client.get(
#     #         path=reverse("comment_view", kwargs={"article_id": 1}),
#     #         HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
#     #     )
#     #     self.assertEqual(response.status_code, status.HTTP_200_OK)
#     #     self.assertEqual(Comment.objects.count(), 5)
#     #     self.assertEqual(len(response.data), 5)
#     # self.assertEqual(response.data[0]["content"], "test content")


# # # view = LikeView, url name = "like_view", method = post
# # class LikeViewTest(APITestCase):
# #     @classmethod
# #     def setUpTestData(cls):
# #         cls.user_data = {"email": "test@test.com", "password": "Test1234!"}
# #         cls.posting_data = {"title": "test Title", "content": "test content"}
# #         cls.user = User.objects.create_user(
# #             "test@test.com", "test", "Test1234!")
# #         cls.posting = Posting.objects.create(**cls.posting_data, user=cls.user)

# #     def setUp(self):
# #         self.access_token = self.client.post(
# #             reverse("token_obtain_pair"), self.user_data
# #         ).data["access"]

# #     # 좋아요 누르기
# #     def test_like_posting(self):
# #         response = self.client.post(
# #             path=reverse("like_view", kwargs={"posting_id": 1}),
# #             HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
# #         )
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)
# #         self.assertEqual(response.data, {'liked': True, 'like_count': 1})

# #     # 좋아요 취소하기
# #     def test_cancel_like_posting(self):
# #         like = Like.objects.create(user=self.user, posting=self.posting)
# #         response = self.client.post(
# #             path=reverse("like_view", kwargs={"posting_id": 1}),
# #             HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
# #         )
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)
# #         self.assertEqual(response.data, {'liked': False, 'like_count': 0})
