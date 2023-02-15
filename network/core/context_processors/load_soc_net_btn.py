from posts.models import SocialNetwork


def social_network(request):
    social_network = social_network = SocialNetwork.objects.all()
    return {
        'social_networks': social_network,
    }
