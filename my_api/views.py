from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.views.generic import CreateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from . import serializers
from .models import Referral as ReferralModel, Referred as ReferredModel
from django.http import Http404
from rest_framework import status
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template import loader



def index(request):
    return render(request, 'referred/referred_done.html', )


class Referral(APIView):
    # permission_classes = (IsAuthenticated, )

    def get(self, request):
        referrals = ReferralModel.objects.all()
        serializer = serializers.ReferralSerializer(referrals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.ReferralSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReferralDetail(APIView):

    def get(self, request, referral_id):
        try:
            referral = ReferralModel.objects.get(pk=referral_id)
        except ReferralModel.DoesNotExist:
            raise Http404
        serializer = serializers.ReferralSerializer(referral)
        return Response(serializer.data)

    def delete(self, request, referral_id):
        try:
            referral = ReferralModel.objects.get(pk=referral_id)
        except ReferralModel.DoesNotExist:
            raise Http404
        referral.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Referred(APIView):

    def get(self, request, referral_id):
        referred = ReferredModel.objects.filter(referral__id=referral_id)
        serializer = serializers.ReferredSerializer(referred, many=True)
        return Response(serializer.data)

    def post(self, request, referral_id):
        try:
            ReferralModel.objects.get(pk=referral_id)
        except ReferralModel.DoesNotExist:
            raise Http404

        serializer = serializers.ReferredSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(referral_id=referral_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReferredDetail(APIView):

    def get(self, request, referral_id, referred_id):
        try:
            referred = ReferredModel.objects.get(referral__id=referral_id, pk=referred_id)
        except ReferredModel.DoesNotExist:
            raise Http404
        serializer = serializers.ReferredSerializer(referred)
        return Response(serializer.data)

    def delete(self, request, referral_id, referred_id):
        try:
            referred = ReferredModel.objects.get(referral__id=referral_id, pk=referred_id)
        except ReferredModel.DoesNotExist:
            raise Http404
        referred.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReferralCreateView(CreateView):
    model = ReferralModel
    template_name = 'referrals/referral_new.html'
    fields = '__all__'


class ReferralDetailView(DetailView):
    model = ReferralModel
    template_name = 'referrals/referral_detail.html'


class ReferralListView(ListView):
    model = ReferralModel
    template_name = 'referrals/home.html'


class ReferredCreateView(CreateView):
    model = ReferredModel
    template_name = 'referred/referred_new.html'
    fields = ('FirstName', 'Surname', 'RefferedPhone', 'Email' )

    def form_valid(self, form):
        form.instance.referral_id = self.kwargs.get('pk')
        form.instance.Status = 'PENDING'
        send_mail('New Cinagi Gap Referral : ' + str(form.instance.FirstName) + ' ' + str(form.instance.Surname) + ' '
                  + str(form.instance.RefferedPhone), str(form.instance.Email), 'noreply@cinagi.co.za',
                  ['admin@cinagi.co.za', ])
        return super(ReferredCreateView, self).form_valid(form)



class ReferredDetailView(DetailView):
    model = ReferredModel
    template_name = 'referred/referred_detail.html'


class ReferredListView(ListView):
    model = ReferredModel
    template_name = 'referred/referred_home.html'


