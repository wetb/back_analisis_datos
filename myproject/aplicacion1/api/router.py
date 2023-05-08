from rest_framework.routers import DefaultRouter
import aplicacion1.api.views as views

router_posts = DefaultRouter()
router_posts.register(prefix='aplicacion1_boyaca',basename='aplicacion1_boyaca',viewset=views.InfoApiViewSet)
router_posts.register(prefix='matriculas_municipio',basename='first_question',viewset=views.FirstApiViewSet)
router_posts.register(prefix='genero_matricula',basename='second_question',viewset=views.SecondApiViewSet)
router_posts.register(prefix='jornada_matricula',basename='third_question',viewset=views.ThirdApiViewSet)
router_posts.register(prefix='ie_matricula',basename='fourth_question',viewset=views.FourthApiViewSet)
router_posts.register(prefix='grado_matricula',basename='fifth_question',viewset=views.FifthApiViewSet)
router_posts.register(prefix='ie_metod',basename='sixth_question',viewset=views.SixthApiViewSet)
