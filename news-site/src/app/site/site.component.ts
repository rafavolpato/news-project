import { Component, ComponentFactoryResolver, Input, OnInit, ɵɵsetComponentScope } from '@angular/core';
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

  constructor(private httpClient: HttpClient) { }

  ngOnInit(): void {
    let params = new HttpParams().set('site', this.site);

    this.httpClient.get<Page>('http://localhost:8000/api/entry/', { params: params, responseType: 'json' }).subscribe(
      res => {
        this.page = new Page(res);
        this.news = this.page.results
        console.log(this.news)
        console.log(typeof(this.news))
      },
      err => {
        console.log(err)
      }
    )

  }

}
