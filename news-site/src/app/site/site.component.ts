import { Component, Input, OnInit } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http'
import { News } from './../nodels/news-model';
import { Page } from '../nodels/page-model';


@Component({
  selector: 'app-site',
  templateUrl: './site.component.html',
  styleUrls: ['./site.component.css']
})
export class SiteComponent implements OnInit {
  @Input() site = '';
  news : News[] = [];
  page: any;
  BASE_URL = 'http://127.0.0.1:8000/api/'

  constructor(private httpClient: HttpClient) { }

  ngOnInit(): void {
    let params = new HttpParams().set('site', this.site);

    this.httpClient.get<Page>(`${this.BASE_URL}entry/`, { params: params, responseType: 'json' }).subscribe({
      next: (res) => {
        this.page = new Page(res);
        this.news = this.page.results
      },
      error: (err) => console.log(err),
    })
  }

  onSave(e: Event): void {
    const element = (e.target as Element)
    this.httpClient.patch<News>(`${this.BASE_URL}entry/${element.id}/`, { responseType: 'json' }).subscribe({
      next: (res) => {
        element.innerHTML =
          `<a target="_blank" href="${res.link}" rel="noopener noreferrer" (click)="onSave($event)" id=${res.id} >
            (${res.click_count} click${res.click_count <= 1 ? '' : 's'}) ${res.title}
          </a>`
      },
      error: (err) => console.log(err),
    })

  }

}
