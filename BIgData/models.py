from typing import Optional
import datetime
import decimal

from sqlalchemy import Column, DECIMAL, DateTime, ForeignKeyConstraint, Index, Integer, Table
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass


class Artist(Base):
    __tablename__ = 'Artist'

    ArtistId: Mapped[int] = mapped_column(Integer, primary_key=True)
    Name: Mapped[Optional[str]] = mapped_column(VARCHAR(120))

    Album: Mapped[list['Album']] = relationship('Album', back_populates='Artist_')


class Employee(Base):
    __tablename__ = 'Employee'
    __table_args__ = (
        ForeignKeyConstraint(['ReportsTo'], ['Employee.EmployeeId'], name='FK_EmployeeReportsTo'),
        Index('IFK_EmployeeReportsTo', 'ReportsTo')
    )

    EmployeeId: Mapped[int] = mapped_column(Integer, primary_key=True)
    LastName: Mapped[str] = mapped_column(VARCHAR(20), nullable=False)
    FirstName: Mapped[str] = mapped_column(VARCHAR(20), nullable=False)
    Title: Mapped[Optional[str]] = mapped_column(VARCHAR(30))
    ReportsTo: Mapped[Optional[int]] = mapped_column(Integer)
    BirthDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    HireDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    Address: Mapped[Optional[str]] = mapped_column(VARCHAR(70))
    City: Mapped[Optional[str]] = mapped_column(VARCHAR(40))
    State: Mapped[Optional[str]] = mapped_column(VARCHAR(40))
    Country: Mapped[Optional[str]] = mapped_column(VARCHAR(40))
    PostalCode: Mapped[Optional[str]] = mapped_column(VARCHAR(10))
    Phone: Mapped[Optional[str]] = mapped_column(VARCHAR(24))
    Fax: Mapped[Optional[str]] = mapped_column(VARCHAR(24))
    Email: Mapped[Optional[str]] = mapped_column(VARCHAR(60))

    Employee: Mapped[Optional['Employee']] = relationship('Employee', remote_side=[EmployeeId], back_populates='Employee_reverse')
    Employee_reverse: Mapped[list['Employee']] = relationship('Employee', remote_side=[ReportsTo], back_populates='Employee')
    Customer: Mapped[list['Customer']] = relationship('Customer', back_populates='Employee_')


class Genre(Base):
    __tablename__ = 'Genre'

    GenreId: Mapped[int] = mapped_column(Integer, primary_key=True)
    Name: Mapped[Optional[str]] = mapped_column(VARCHAR(120))

    Track: Mapped[list['Track']] = relationship('Track', back_populates='Genre_')


class MediaType(Base):
    __tablename__ = 'MediaType'

    MediaTypeId: Mapped[int] = mapped_column(Integer, primary_key=True)
    Name: Mapped[Optional[str]] = mapped_column(VARCHAR(120))

    Track: Mapped[list['Track']] = relationship('Track', back_populates='MediaType_')


class Playlist(Base):
    __tablename__ = 'Playlist'

    PlaylistId: Mapped[int] = mapped_column(Integer, primary_key=True)
    Name: Mapped[Optional[str]] = mapped_column(VARCHAR(120))

    Track: Mapped[list['Track']] = relationship('Track', secondary='PlaylistTrack', back_populates='Playlist_')


class Album(Base):
    __tablename__ = 'Album'
    __table_args__ = (
        ForeignKeyConstraint(['ArtistId'], ['Artist.ArtistId'], name='FK_AlbumArtistId'),
        Index('IFK_AlbumArtistId', 'ArtistId')
    )

    AlbumId: Mapped[int] = mapped_column(Integer, primary_key=True)
    Title: Mapped[str] = mapped_column(VARCHAR(160), nullable=False)
    ArtistId: Mapped[int] = mapped_column(Integer, nullable=False)

    Artist_: Mapped['Artist'] = relationship('Artist', back_populates='Album')
    Track: Mapped[list['Track']] = relationship('Track', back_populates='Album_')


class Customer(Base):
    __tablename__ = 'Customer'
    __table_args__ = (
        ForeignKeyConstraint(['SupportRepId'], ['Employee.EmployeeId'], name='FK_CustomerSupportRepId'),
        Index('IFK_CustomerSupportRepId', 'SupportRepId')
    )

    CustomerId: Mapped[int] = mapped_column(Integer, primary_key=True)
    FirstName: Mapped[str] = mapped_column(VARCHAR(40), nullable=False)
    LastName: Mapped[str] = mapped_column(VARCHAR(20), nullable=False)
    Email: Mapped[str] = mapped_column(VARCHAR(60), nullable=False)
    Company: Mapped[Optional[str]] = mapped_column(VARCHAR(80))
    Address: Mapped[Optional[str]] = mapped_column(VARCHAR(70))
    City: Mapped[Optional[str]] = mapped_column(VARCHAR(40))
    State: Mapped[Optional[str]] = mapped_column(VARCHAR(40))
    Country: Mapped[Optional[str]] = mapped_column(VARCHAR(40))
    PostalCode: Mapped[Optional[str]] = mapped_column(VARCHAR(10))
    Phone: Mapped[Optional[str]] = mapped_column(VARCHAR(24))
    Fax: Mapped[Optional[str]] = mapped_column(VARCHAR(24))
    SupportRepId: Mapped[Optional[int]] = mapped_column(Integer)

    Employee_: Mapped[Optional['Employee']] = relationship('Employee', back_populates='Customer')
    Invoice: Mapped[list['Invoice']] = relationship('Invoice', back_populates='Customer_')


class Invoice(Base):
    __tablename__ = 'Invoice'
    __table_args__ = (
        ForeignKeyConstraint(['CustomerId'], ['Customer.CustomerId'], name='FK_InvoiceCustomerId'),
        Index('IFK_InvoiceCustomerId', 'CustomerId')
    )

    InvoiceId: Mapped[int] = mapped_column(Integer, primary_key=True)
    CustomerId: Mapped[int] = mapped_column(Integer, nullable=False)
    InvoiceDate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)
    Total: Mapped[decimal.Decimal] = mapped_column(DECIMAL(10, 2), nullable=False)
    BillingAddress: Mapped[Optional[str]] = mapped_column(VARCHAR(70))
    BillingCity: Mapped[Optional[str]] = mapped_column(VARCHAR(40))
    BillingState: Mapped[Optional[str]] = mapped_column(VARCHAR(40))
    BillingCountry: Mapped[Optional[str]] = mapped_column(VARCHAR(40))
    BillingPostalCode: Mapped[Optional[str]] = mapped_column(VARCHAR(10))

    Customer_: Mapped['Customer'] = relationship('Customer', back_populates='Invoice')
    InvoiceLine: Mapped[list['InvoiceLine']] = relationship('InvoiceLine', back_populates='Invoice_')


class Track(Base):
    __tablename__ = 'Track'
    __table_args__ = (
        ForeignKeyConstraint(['AlbumId'], ['Album.AlbumId'], name='FK_TrackAlbumId'),
        ForeignKeyConstraint(['GenreId'], ['Genre.GenreId'], name='FK_TrackGenreId'),
        ForeignKeyConstraint(['MediaTypeId'], ['MediaType.MediaTypeId'], name='FK_TrackMediaTypeId'),
        Index('IFK_TrackAlbumId', 'AlbumId'),
        Index('IFK_TrackGenreId', 'GenreId'),
        Index('IFK_TrackMediaTypeId', 'MediaTypeId')
    )

    TrackId: Mapped[int] = mapped_column(Integer, primary_key=True)
    Name: Mapped[str] = mapped_column(VARCHAR(200), nullable=False)
    MediaTypeId: Mapped[int] = mapped_column(Integer, nullable=False)
    Milliseconds: Mapped[int] = mapped_column(Integer, nullable=False)
    UnitPrice: Mapped[decimal.Decimal] = mapped_column(DECIMAL(10, 2), nullable=False)
    AlbumId: Mapped[Optional[int]] = mapped_column(Integer)
    GenreId: Mapped[Optional[int]] = mapped_column(Integer)
    Composer: Mapped[Optional[str]] = mapped_column(VARCHAR(220))
    Bytes: Mapped[Optional[int]] = mapped_column(Integer)

    Playlist_: Mapped[list['Playlist']] = relationship('Playlist', secondary='PlaylistTrack', back_populates='Track')
    Album_: Mapped[Optional['Album']] = relationship('Album', back_populates='Track')
    Genre_: Mapped[Optional['Genre']] = relationship('Genre', back_populates='Track')
    MediaType_: Mapped['MediaType'] = relationship('MediaType', back_populates='Track')
    InvoiceLine: Mapped[list['InvoiceLine']] = relationship('InvoiceLine', back_populates='Track_')


class InvoiceLine(Base):
    __tablename__ = 'InvoiceLine'
    __table_args__ = (
        ForeignKeyConstraint(['InvoiceId'], ['Invoice.InvoiceId'], name='FK_InvoiceLineInvoiceId'),
        ForeignKeyConstraint(['TrackId'], ['Track.TrackId'], name='FK_InvoiceLineTrackId'),
        Index('IFK_InvoiceLineInvoiceId', 'InvoiceId'),
        Index('IFK_InvoiceLineTrackId', 'TrackId')
    )

    InvoiceLineId: Mapped[int] = mapped_column(Integer, primary_key=True)
    InvoiceId: Mapped[int] = mapped_column(Integer, nullable=False)
    TrackId: Mapped[int] = mapped_column(Integer, nullable=False)
    UnitPrice: Mapped[decimal.Decimal] = mapped_column(DECIMAL(10, 2), nullable=False)
    Quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    Invoice_: Mapped['Invoice'] = relationship('Invoice', back_populates='InvoiceLine')
    Track_: Mapped['Track'] = relationship('Track', back_populates='InvoiceLine')


t_PlaylistTrack = Table(
    'PlaylistTrack', Base.metadata,
    Column('PlaylistId', Integer, primary_key=True),
    Column('TrackId', Integer, primary_key=True),
    ForeignKeyConstraint(['PlaylistId'], ['Playlist.PlaylistId'], name='FK_PlaylistTrackPlaylistId'),
    ForeignKeyConstraint(['TrackId'], ['Track.TrackId'], name='FK_PlaylistTrackTrackId'),
    Index('IFK_PlaylistTrackPlaylistId', 'PlaylistId'),
    Index('IFK_PlaylistTrackTrackId', 'TrackId')
)
